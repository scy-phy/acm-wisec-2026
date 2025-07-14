+++
title = "Replicability Label"
hidden = true
[menu.main]
#    parent = "For Authors"
    weight = 2040
+++

# Replicability Label

The organizing committee of the 2022 ACM WiSec Symposium is pleased to offer accepted papers the opportunity to have their research artifacts certified as reproducible and archived for posterity. This effort continues the effort pioneered in 2017 towards supporting greater reproducibility in mobile and wireless security experimental research. The goal of this process is to increase the impact of mobile and wireless security research, enable dissemination of research results, code and experimental setups, and to enable the research community to build on prior experimental results. We recognize papers whose experimental results were replicated by an independent committee and provide a “replicability label” in accordance with the terminology defined by ACM.

Authors of accepted papers can participate in this voluntary process by submitting supporting evidence of their experiments’ replicability, following the instructions below. Authors are encouraged to plan ahead when running their experiments, in order to minimize the overhead of applying for this label.


## Review Process in Brief

The authors upload a VM containing all the necessary data and code required to replicate the results. At least two reviewers are asked to replicate the results for each submission. We ensure that the VMs are self-contained to the maximum extent possible to eliminate any future version deprecation and backward compatibility issues. The reviewers clarify any issues directly with the authors (and may request updates to the original VM and code).

The submission deadline for replicability applications is **March 25, 2022 (23:59 AoE)**. This is one calendar week before the artifact notification date.

Authors will be notified if their work was replicated by  **April 1, 2022 (23:59 AoE)**. This is one day business day before the camera-ready deadline.

If the committee can verify that all relevant data sets were included and the graphs/tables can be regenerated based on this, the committee will grant a replicability label and also provide a report on the regeneration process.

Due to the narrow time window to validate artifacts, authors are strongly encouraged to **submit packages early**. Submissions that successfully replicate and are submitted more than 24 hours before the deadline will receive a very nice certificate of appreciation from the replication co-chairs. Submitting early will provide more opportunities for communication and clarification with reviewers if necessary, but will otherwise not prejudice the evaluation. All submissions before the official deadline will be evaluated independently on their own merits.


## Preparing a Replicability Application

- Prepare a VirtualBox VM with all data/tools installed. It is expected that the authors include within this VM raw data (without any pre-processing) and all the scripts used for pre-processing.
- For each graph/table, provide a directory (Fig_XXX, Table_XXX) which contains a script that enables the committee to regenerate that object.
- Include in the home directory a README file, according to the following format template: {{<link target="_blank" href="cfp/replicability/README.txt">}}README.txt {{<fas "file-alt">}}{{</link>}}. 
You will also be asked to submit this file separately with the application.
- Provide a link to downloading the VM (e.g. Google Drive or Dropbox), or request credentials to upload the VM to the conference storage system.
- ~~Submit the result to the replicability HotCRP instance.~~
<!-- - ~~Submit the result to the replicability HotCRP instance: https://wisec22-artifacts.hotcrp.com/.~~ -->

We encourage you to also release your code (e.g. on GitHub) and data (e.g. on Zenodo) independently of the submitted VM. If you do so, feel free to submit links to these releases together with the VM.

If you have any questions about the submission process or preparing your work for evaluation, feel free to email the artifact evaluation co-chairs (listed below). We are happy to take these questions and want authors to feel confident that the package they submit is what is needed for a successful evaluation.


## Volunteer to Review Replication Submissions

A replication review process requires a number of volunteers to actually review the submissions. New for 2022, we are actively seeking nominations for volunteers to participate. Self-nominations are welcome!

~~You can submit a nomination before **March 25, 2022** at this link.~~
<!-- ~~You can submit a nomination before **March 25, 2022** at this link: https://forms.gle/N7k2AkuKkbMJJaVb7 ~~ -->

Replication volunteers are typically graduate student researchers, but interested undergraduates or other interested parties are welcome to apply. The main requirements are: 1) the ability to receive a package of software and follow the directions to build and run it; 2) some facility with debugging software you didn’t write; and 3) significant availability between March 25 and April 1, 2022. WiSec 22 accepted paper authors are welcome to participate in this process, though they will not be able to participate in the review of their own submissions.

Benefits of reviewing replications include:
- The pride and joy of serving the WiSec community and the greater cause of open and replicable science
- Recognition for service on this website (also suitable for mention on a CV/resume – impress your friends!)
- A look “behind the scenes” of the replication process to help you learn what is expected in a replication package and how to improve your own future replication submissions.


## Replicability Committee
- David Barrera, *Carleton University, Ontario, Canda* (Co-Chair)
- Bradley Reaves, *North Carolina State University, Raleigh, North Carolina, USA* (Co-Chair)
- Conner Bradley, *Carleton University, Canada*
- Dong Chen, *Peking University, China*
- Harshvardhan Takawale, *Singapore University of Technology and Design, Singapore*
- Imranur Rahman, *North Carolina State University, USA*
- Imtiaz Karim, *Purdue University, USA*
- Kevin Guy, *Carleton University, Canada*
- Sathvik Prasad, *North Carolina State University, USA*
- Shaohu Zhang, *North Carolina State University, USA*
- Zhibo Liu, *Hong Kong University of Science and Technology, Hong Kong*
- Zongjie Li, *Hong Kong University of Science and Technology, Hong Kong*
- Raveen Wijewickrama, *University of Texas at San Antonio, Texas, USA*
- Naureen Hoque, *Rochester Institute of Technology, USA*
<!-- - ~~*Your name here!*~~ -->

## Publication of Data and Reproducible Environments

The VMs will be made available, as always, on the ACM WiSec datasets server at
{{<link target="_blank" rel="noopener" href="http://wisecdata.ccs.neu.edu/" >}}wisecdata.ccs.neu.edu{{</link>}}
after the conference.


## Replicable Publications

<!-- Validated papers will be awarded the ACM badges for: -->
The following papers are awarded with the ACM badges for:
<div style="display: table;">
    <div style="display: table-row; vertical-align: middle;">
        <div style="display: table-cell; vertical-align: middle; padding-right:10px; padding-bottom: 15px">
            {{< image src="images/badges/artifacts_evaluated_functional_dl.jpg" title="Artifacts Evaluated – Functional" alt="Artifacts Evaluated – Functional" >}}
        </div>
        <div style="display: table-cell; vertical-align: middle; padding-bottom: 15px">
            <b>Artifacts Evaluated – Functional</b><br>
            The artifacts associated with the paper are of a quality that significantly exceeds minimal functionality. 
            That is, they have all the qualities of the Artifacts Evaluated – Functional level, but, in addition, they are very carefully documented and well-structured 
            to the extent that reuse and repurposing is facilitated. In particular, norms and standards of the research community for artifacts of this type are strictly 
            adhered to. 
        </div>
    </div>
    <div style="display: table-row; vertical-align: middle">
        <div style="display: table-cell; vertical-align: middle; padding-right:10px; padding-bottom: 15px">
            {{< image src="images/badges/artifacts_available_dl.jpg" title="Artifacts Available" alt="Artifacts Available" >}}
        </div>
        <div style="display: table-cell; vertical-align: middle; padding-bottom: 15px">
            <b>Artifacts Available</b><br>
            Author-created artifacts relevant to this paper have been placed on a publically accessible archival repository. A DOI or link to this repository 
            along with a unique identifier for the object is provided.
        </div>
    </div>
   <div style="display: table-row; vertical-align: middle">
        <div style="display: table-cell; vertical-align: middle; padding-right:10px; padding-bottom: 15px">
            {{< image src="images/badges/results_reproduced_dl.jpg" title="Results Reproduced" alt="Results Reproduced" >}}
        </div>
        <div style="display: table-cell; vertical-align: middle; padding-bottom: 15px">
            <b>Results Reproduced</b><br>
            The main results of the paper have been obtained in a subsequent study by a person or team other than the authors, using, 
            in part, artifacts provided by the author.
        </div>
    </div>
</div>

<ul>
<li>
{{< publication-links crossref="accepted-papers/" 
title="Automating the Quantitative Analysis of Reproducibility for Build Artifacts derived from the Android Open Source Project"
>}}
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_evaluated_functional_dl.jpg">
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_available_dl.jpg">
<img style="margin-bottom: 4px" height="25px" src="/images/badges/replicability-badge.png">

<li>
{{< publication-links crossref="accepted-papers/" 
    title="AirGuard - Protecting Android Users From Stalking Attacks By Apple Find My Devices"
>}}
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_evaluated_functional_dl.jpg">
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_available_dl.jpg">
<img style="margin-bottom: 4px" height="25px" src="/images/badges/replicability-badge.png">
</li>

<li>
{{< publication-links crossref="accepted-papers/" 
    title="Device Re-identification in LoRaWAN through Messages Linkage"
>}}
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_evaluated_functional_dl.jpg">
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_available_dl.jpg">
<img style="margin-bottom: 4px" height="25px" src="/images/badges/replicability-badge.png">
</li>

<li>
{{< publication-links crossref="accepted-papers/" 
    title="Evil Never Sleeps: When Wireless Malware Stays On After Turning Off iPhones"
>}}
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_evaluated_functional_dl.jpg">
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_available_dl.jpg">
<img style="margin-bottom: 4px" height="25px" src="/images/badges/replicability-badge.png">
</li>

<li>
{{< publication-links crossref="accepted-papers/" 
    title="Take a Bite of the Reality Sandwich: Revisiting the Security of Progressive Message Authentication <br>Codes"
>}}
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_evaluated_functional_dl.jpg">
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_available_dl.jpg">
<img style="margin-bottom: 4px" height="25px" src="/images/badges/replicability-badge.png">
</li>

<li>
{{< publication-links crossref="accepted-papers/" 
    title="PITracker: Detecting Android PendingIntent Vulnerabilities through Intent Flow Analysis"
>}}
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_available_dl.jpg">
</li>

<li>
{{< publication-links crossref="accepted-papers/" 
    title="PAcT: Detecting and Classifying Privacy Behavior of Android Applications"
>}}
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_available_dl.jpg">
</li>

<li>
{{< publication-links crossref="accepted-papers/" 
    title="BP-MAC: Fast Authentication for Short Messages"
>}}
<img style="margin-bottom: 4px" height="25px" src="/images/badges/artifacts_available_dl.jpg">
</li>

</ul>
