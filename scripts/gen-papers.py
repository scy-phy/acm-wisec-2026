import pandas as pd
import argparse
from collections import namedtuple
from html.parser import HTMLParser
from typing import List, Tuple, Optional

TOCEntry = namedtuple('TOCEntry', ['title', 'acm_url', 'authors', 'abstract'])

def simplify_title(title):
	title = ''.join([c.lower() for c in title if c.isalnum()][:20])
	title = ' '.join(title.split())
	return title

class TocHTMLParser(HTMLParser):
	def __init__(self) -> None:
		super().__init__()
		self.data = []
		self.url = ""
		self.authors = []

		self.flag_title = False
		self.flag_authors = False
		self.flag_last_authors = False
		self.flag_abstract = [False, False]

	def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
		if tag == 'a' and attrs[0] == ("class", "DLtitleLink"):
			self.flag_title = True
			self.url = attrs[3][1]
		if tag == 'li' and attrs[0][0] == "class" and attrs[0][1][:8] == "nameList":
			self.flag_authors = True
			if attrs[0][1][-4:] == "Last":
				self.flag_last_authors = True
		if tag == 'div' and attrs[0] == ("style", "display:inline"):
			self.flag_abstract[0] = True
		if self.flag_abstract[0] and tag == 'p':
			self.flag_abstract[1] = True

	def handle_endtag(self, tag: str) -> None:
		if self.flag_abstract[0] and tag == 'div':
			self.flag_abstract[0] = False
	
	def handle_data(self, data: str) -> None:
		if self.flag_title:
			title = ' '.join(data.split())
			self.data.append([title])
			self.data[-1].append(self.url)
			self.flag_title = False
		if self.flag_authors:
			data = data.strip()
			if not data:
				return None
			self.authors.append(data)
			if self.flag_last_authors:
				self.data[-1].append(self.authors)
				self.authors = []
				self.flag_authors = False
				self.flag_last_authors = False
		if self.flag_abstract[1]:
			self.data[-1].append(' '.join(data.split()))
			self.flag_abstract[1] = False

	def close(self) -> None:
		return super().close(), self.data

def parse_toc(toc_html):
	with open(toc_html, 'r') as f:
		html_content = f.read()
	parser = TocHTMLParser()
	parser.feed(html_content)
	_, result = parser.close()
	result_dict = {}
	for entry in result:
		title = entry[0]
		acm_url = entry[1]
		authors = entry[2]
		abstract = '\n\n'.join(entry[3:])
		result_dict[simplify_title(title)] = TOCEntry(title, acm_url, authors, abstract)
	return result, result_dict

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--data", required=True, help="wiseml_toc.html | wisec21-authors.csv")
	args = parser.parse_args()

	if args.data == "wiseml_toc.html":
		toc, _ = parse_toc("wiseml_toc.html")
		for entry in toc:
			title = entry[0]
			acm_url = entry[1]
			authors = entry[2]
			abstract = '\n\n'.join(entry[3:])

			print("{{< publication")
			print(f"\ttitle=\"{title}\"\n")

			i = 1
			for author in authors:
				print(f"\tauthor{i}=\"{author.strip()} #\"")
				i += 1

			print()
			print(f'\tacm="{acm_url}"')

			print(">}}")
			print('{{< spoiler text="Show abstract" >}}')
			print(f'{abstract}')
			print('{{< /spoiler >}}\n')
		# for line in open("wiseml21.csv"):
		# 	num, title, authors = line.split(";")

		# 	print("{{< publication")
		# 	print(f"\ttitle=\"{title}\"\n")

		# 	i = 1
		# 	for author in authors.split(", "):
		# 		print(f"\tauthor{i}=\"{author.strip()} #\"")
		# 		i += 1
			
		# 	print()
		# 	print(f'acm="{toc[simplify_title(title)]}"')

		# 	print("\n>}}")
	elif args.data == "wisec21-authors.csv":
		_, toc = parse_toc("wisec_toc.html")
		flag_title_and_url_only = True

		with open('papers-with-abstracts.txt') as f:
			lines = f.readlines()
		abstracts_beg = [i+2 for i in range(len(lines)) if lines[i] == "Abstract\n"]
		abstracts_end = [i-1 for i in range(len(lines)) if lines[i] == "Authors\n"]
		abstracts = [lines[b:e] for b,e, in zip(abstracts_beg, abstracts_end)]
		for i in range(len(abstracts)):
			for j in range(len(abstracts[i])):
				if abstracts[i][j] != "\n":
					abstracts[i][j] = abstracts[i][j].strip()
				else:
					abstracts[i][j] = "\n\n"
			abstracts[i] = ' '.join(abstracts[i])
		abs_iter = iter(abstracts)

		df_wisec21 = pd.read_csv(args.data)
		papers_grouped = df_wisec21.groupby('paper')
		for _, grp in papers_grouped:
			if flag_title_and_url_only:
				tocentry = toc[simplify_title(grp.title.iloc[0])] 
				# if tocentry.title != grp.title.iloc[0]:
				# 	print(f'toc title: {tocentry.title}')
				# 	print(f'csv title: {grp.title.iloc[0]}')
				print(tocentry.title)
				print(f'\tacm="{tocentry.acm_url}"')
				continue
			print("{{< publication")
			print(f"\ttitle=\"{grp.title.iloc[0]}\"\n")

			aff_dict = {}
			i = 1
			for row in grp.itertuples():
				if row.affiliation not in aff_dict:
					aff_dict[row.affiliation] = i
					i += 1

			i = 1
			for row in grp.itertuples():
				print(f"\tauthor{i}=\"{row.first} {row.last} #{aff_dict[row.affiliation]}\"")
				i += 1
			print()

			aff_dict_rev = {v: k for k, v in aff_dict.items()}
			for i in range(len(aff_dict_rev)):
				print(f'\taffiliation{i+1}="{aff_dict_rev[i+1]}"')
				i += 1

			print(">}}")
			print('{{< spoiler text="Show abstract" >}}')
			print(f'{next(abs_iter)}')
			print('{{< /spoiler >}}\n')
	else:
		print("Error! Wrong input csv file.")


