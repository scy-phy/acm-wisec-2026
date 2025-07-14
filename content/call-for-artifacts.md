+++
title = "Call for Artifacts"
# hidden = true
[menu.main]
    parent = "Call for"
    weight = 3000
+++
# Call for Artifacts

The organizing committee of the 2025 ACM WiSec Symposium is pleased to offer accepted papers the opportunity to have their research artifacts certified as replicable and archived for posterity. This effort continues the effort pioneered in 2017 towards supporting greater reproducibility in mobile and wireless security experimental research. The goal of this process is to increase the impact of mobile and wireless security research, enable dissemination of research results, code and experimental setups, and to enable the research community to build on prior experimental results. We recognize papers whose experimental results were replicated by an independent committee and provide a “badge” in accordance with the [terminology defined by ACM](https://www.acm.org/publications/policies/artifact-review-and-badging-current).

Authors of accepted papers can participate in this voluntary process by submitting supporting evidence of their experiments’ replicability, following the instructions below. Authors are encouraged to plan ahead when running their experiments, in order to minimize the overhead of applying for these badges.

## Review Process in Brief

The authors upload a VM containing all the necessary data and code required to replicate the results. At least two reviewers are asked to replicate the results for each submission. Authors ensure that submitted VMs are self-contained to the maximum extent possible to eliminate any future version deprecation and backward compatibility issues. The reviewers clarify any issues directly with the authors (and may request updates to the original VM and code).

The submission deadline for replicability applications is **May 15, 2025 (23:59 AoE)**.

Authors will be notified if their work was replicated by **May 24, 2025 (23:59 AoE)**.

If the committee can verify that all relevant data sets were included and the graphs/tables can be regenerated based on this, the committee will grant a replicability badge and also provide a report on the regeneration process.

Due to the narrow time window to validate artifacts, authors are strongly encouraged to **submit packages early**. Submitting early will provide more opportunities for communication and clarification with reviewers if necessary, but will otherwise not prejudice the evaluation. All submissions before the official deadline will be evaluated independently on their own merits.

## Preparing an Artifact Submission

- Prepare a VirtualBox VM with all data/tools installed. It is expected that the authors include within this VM raw data (without any pre-processing) and all the scripts used for pre-processing.
- For each graph/table, provide a directory (Fig_XXX, Table_XXX) which contains a script that enables the committee to regenerate that object.
- Include in the home directory a README file, according to the following format template: [README.txt](/artifacts/README.txt). You will also be asked to submit this file separately with the application.
- Provide a link to downloading the VM (e.g. Google Drive or Dropbox), or request credentials to upload the VM to the conference storage system.
- Submit the result to the HotCRP [https://wisec25replicability.hotcrp.com/](https://wisec25replicability.hotcrp.com/)

We encourage you to also release your code (e.g. on GitHub) and data (e.g. on Zenodo) independently of the submitted VM. If you do so, feel free to submit links to these releases together with the VM.

If you have any questions about the submission process or preparing your work for evaluation, feel free to email the artifact evaluation co-chairs (listed below). We are happy to take these questions and want authors to feel confident that the package they submit is what is needed for a successful evaluation.

## Volunteer to Review Submissions

Thanks for your interest! We are currently looking for volunteers.

Artifact evaluation volunteers are typically graduate student researchers, but interested undergraduates or other interested parties are welcome to apply. The main requirements are: 1) the ability to receive a package of software and follow the directions to build and run it; 2) some ability with debugging software you didn’t write; and 3) significant availability between May 1 and May 10, 2025. WiSec 25 accepted paper authors are welcome to participate in this process, though they will not be able to participate in the review of their own submissions.

Benefits of reviewing submissions include:

- The pride and joy of serving the WiSec community and the greater cause of open and replicable science
- Recognition for service on this website (also suitable for mention on a CV/resume – impress your friends!)
- A look “behind the scenes” of the replication process to help you learn what is expected in a replication package and how to improve your own future replication submissions.

## Artifact Evaluation Committee

- Aanjhan Ranganathan, Northeastern University, United States (Co-Chair)
- Altaf Shaik, TU Berlin, Germany  (Co-Chair)
- Harshad Sathaye, ETH Zurich, Switzerland  (Co-Chair)
- Arslan Mumtaz, CISPA @ Helmholtz Center for Information Security, Germany
- Christopher Tibaldo, SwissGrid, Switzerland
- Claudio Anliker, ETH Zurich, Switzerland
- Graciana Aad, ETH Zurich, Switzerland
- Maryam Motallebighomi, Northeastern University, United States
- Sebastian Neef, TU-Berlin, Germany
- Vincent Ulitzsch, TU-Berlin, Germany

## Publication of Data and Reproducible Environments

The VMs will be made available, as always, on the ACM WiSec datasets server at [http://wisecdata.ccs.neu.edu/](http://wisecdata.ccs.neu.edu/) after the conference.
