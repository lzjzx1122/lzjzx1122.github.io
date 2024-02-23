---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
.pubtitle{
    background: #BD666D;
    color: white;
    font-size: 12px;
    padding: 1px 5px 1px 5px;
    border-radius: 15px;
    float: left;
    font-weight: bold;
}
.font-bold{
    font-weight:bolder;
}
</style>

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am now a Postdoc at [Emerging Parallel Computing Center (EPCC)](http://epcc.sjtu.edu.cn) and a visiting scholar at NTU (Nanyang Technological University) [S-Lab](https://personal.ntu.edu.sg/tianwei.zhang/supervision.html). I obtained my Ph.D. from Shanghai Jiao Tong University (SJTU) under the supervision of [Prof. Quan Chen](https://www.cs.sjtu.edu.cn/~chen-quan/index_EN.html) and [Prof. Minyi Guo](https://cs.sjtu.edu.cn/~guo-my/). Before that, I received Bachelor degree at School of Information and Software Engineering, University Of Electronic Science And Technology Of China (UESTC). My research interests include Cloud-Native System and General-purpose Serverless Computing, particularly how to design serverless systems and provide elastic resource management for workflows and stateful functions. If you are interested in my project details, feel free to email me. 

<!-- My research interest includes neural machine translation and computer vision. I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>). -->


<!-- # 🔥 News -->
<!-- # News
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

<!-- # 📝 Publications  -->
# Publications  

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

**Kaiming He**, Xiangyu Zhang, Shaoqing Ren, Jian Sun

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div> -->
<div>
(*Corresponging Author)
</div>
<ul>
<li><div class="pubtitle">ASPLOS 2024</div> &nbsp;<a href="https://arxiv.org/abs/2304.14629">DataFlower: Exploiting the Data-flow paradigm For Serverless Workflow Orchestration.</a> <span class="font-bold">Zijun Li</span>, Chuhao Xu, Quan Chen*, Jieru Zhao, Chen Chen, Minyi Guo*. (Accept to appear)</li>
<li><div class="pubtitle">ASPLOS 2024</div> &nbsp;<a href="/">FaaSGraph: Enabling Scalable, Efficient, and Cost-Effective Graph Processing with Serverless Computing.</a> Yushi Liu, Shixuan Sun, <span class="font-bold">Zijun Li</span>, Quan Chen*, Sen Gao, Bingsheng He, Chao Li, Minyi Guo*. (Accept to appear)</li>
<li><div class="pubtitle">ICPADS 2023 Best Paper</div> &nbsp;<a href="/">Microless: Cost-Efficient Hybrid Deployment of Microservices on IaaS VMs and Serverless.</a> Jiagan Cheng; Yilong Zhao; <span class="font-bold">Zijun Li</span>; Quan Chen*; Weihao Cui; Minyi Guo*.</li>
<li><div class="pubtitle">SoCC 2023</div> &nbsp;<a href="/">Maximizing the Utilization of GPUs Used by Cloud Gaming through Adaptive Co-location with Combo.</a> Binghao Chen, Han Zhao*, Weihao Cui, Yifu He, Shulai Zhang, Quan Chen*, <span class="font-bold">Zijun Li</span>, Minyi Guo*.</li>
<li><div class="pubtitle">USENIX ATC 2022</div> &nbsp;<a href="https://www.usenix.org/conference/atc22/presentation/li-zijun-rund">RunD: A Lightweight Secure Container Runtime for High-density Deployment and High-concurrency Startup in Serverless Computing.</a> <span class="font-bold">Zijun Li</span>, Jiagan Cheng, Quan Chen*, Eryu Guan, Zizheng Bian, Yi Tao, Bin Zha, QiangWang, Weidong Han, Minyi Guo*.</li>
<li><div class="pubtitle">USENIX ATC 2022</div> &nbsp;<a href="https://www.usenix.org/conference/atc22/presentation/li-zijun-help">Help Rather Than Recycle: Alleviating Cold Startup in Serverless Computing Through Inter-Function Container Sharing.</a> <span class="font-bold">Zijun Li</span>, Linsong Guo, Quan Chen*, Jiagan Cheng, Chuhao Xu, Deze Zeng, Zhuo Song, Tao Ma, Yong Yang, Chao Li, Minyi Guo*.</li>
<li><div class="pubtitle">ASPLOS 2022</div> &nbsp;<a href="https://dl.acm.org/doi/abs/10.1145/3503222.3507717">FaaSFlow: Enable Efficient Workflow Execution For Function-as-a-Service.</a> <span class="font-bold">Zijun Li</span>, Yushi Liu, Linsong Guo, Quan Chen*, Jiagan Cheng, Wenli Zheng, Minyi Guo*.</li>
<li><div class="pubtitle">ACM Comput. Surv.</div> &nbsp;<a href="https://dl.acm.org/doi/abs/10.1145/3508360">The Serverless Computing Survey: A Technical Primer for Design Architecture.</a> <span class="font-bold">Zijun Li</span>, Linsong Guo, Jiagan Cheng, Quan Chen*, BingSheng He, Minyi Guo*.</li>
<li><div class="pubtitle">IPDPS 2020</div> &nbsp;<a href="https://ieeexplore.ieee.org/abstract/document/9139803">Amoeba: Qos-awareness and Reduced Resource Usage of Microservices with Serverless Computing.</a> <span class="font-bold">Zijun Li</span>, Quan Chen*, Shuai Xue, Tao Ma, Yong Yang, Zhuo Song, Minyi Guo*.</li>
<li><div class="pubtitle">中国科学：信息科学</div> &nbsp;<a href="https://www.sciengine.com/SSI/doi/10.1360/SSI-2023-0155">Serverless computing based on dynamic-addressable session.一种基于动态可寻址会话的服务器无感知计算.</a> <span class="font-bold">李子俊</span>, 赵一龙, 陈全*, 过敏意*.</li>
</ul>

<a href='https://scholar.google.com/citations?user=cHjjhw0AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=Total google scholar citations"></a>

# Honors and Awards
- *2023.09* : Outstanding Ph.D. Scholarship of Yang Yuanqing Education Fund
- *2022.09* : Ph.D. National Scholarship
<!-- # 🎖 Honors and Awards -->

# Experiences
- *2023.12 - Now*, Visiting Scholar - School of Computer Science and Engineering, Nanyang Technological University 
- *2023.09 - Now*, Postdoc - Department of Computer Science and Engineering, Shanghai Jiao Tong University. 
- *2021.04 - 2022.04*, Research Intern - Alibaba Cloud. 
- *2018.09 - 2023.09*, Ph.D - Department of Computer Science and Engineering, Shanghai Jiao Tong University. 
- *2014.09 - 2018.06*, Bachelor - School of Information and Software Engineering, University Of Electronic Science And Technology Of China.
<!-- # 📖 Educations -->

<!-- # Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2016.11*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->
<!-- # 💬 Invited Talks -->


<!-- # Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China. -->
<!-- # 💻 Internships -->

<hr>
<img alt="last updated" src="https://img.shields.io/github/last-commit/lzjzx1122/lzjzx1122.github.io?color=e8e8e8&label=Last%20Updated&logo=Convertio&logoColor=white&style=flat-square&labelColor=gray">  &nbsp;

<a href="http://s01.flagcounter.com/more/gWC"><img src="https://s01.flagcounter.com/count2/gWC/bg_F5F5F5/txt_000000/border_8C8C8C/columns_4/maxflags_8/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>

