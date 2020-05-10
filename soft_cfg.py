import json

version = 1.3
name = "toodoAssistant.exe"
welcome = "赠卿春绿夏黄秋红，余生卿欠我白首"

# 定义网址
web_site = "https://www.toodo.fun"  # 网站主页
api_site = "https://www.toodo.fun/api" # API 主页
feed_back = "https://www.toodo.fun"  # 反馈网址
help_us = "https://toodo.fun/funs/thanks/"  # 捐赠网址
source_api_url = "http://softapi.toodo.fun/get_source"  # 源码仓库网址
article_api_url = "http://softapi.toodo.fun/get_article"  # 文章教程网址
update_url = "https://www.toodo.fun/api/software/version.php"  # 软件更新网址

# 线程配置
time_thread = .5
source_thread = 600  # 不用经常刷新
article_thread = 60

# 测试数据
debug = 0
source_api = json.dumps(
    {'url': ['https://github.com//MR5356/bilibili-up-helper', 'https://github.com//MR5356/MRweidiannao'],
     'title': ['bilibili-up-helper', 'MRweidiannao'], 'info': ['A helper for bilibili uploader', '微电脑安卓APP（已暂停服务）'],
     'language': ['Python', 'Java']})
article_api = json.dumps({'url': [
    'https://toodo.fun/funs/learn/files/article.php?id=58&title=UP%E4%B8%BB%E5%B0%8F%E5%8A%A9%E6%89%8B%20%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E'],
                          'title': ['UP主小助手 使用说明'],
                          'info': ['《UP主小助手 使用说明》是作者 鱼鹰的酒鬼 最后更新于 2020-04-24 的一篇文章，当前阅读量为 1632'],
                          'date': ['2020-04-24']})

licenses = '''<h2 id="mozillapubliclicenseversion20">Mozilla Public License Version 2.0</h2>
<h3 id="1definitions">1. Definitions</h3>
<p>1.1. "Contributor"
    means each individual or legal entity that creates, contributes to
    the creation of, or owns Covered Software.</p>
<p>1.2. "Contributor Version"
    means the combination of the Contributions of others (if any) used
    by a Contributor and that particular Contributor's Contribution.</p>
<p>1.3. "Contribution"
    means Covered Software of a particular Contributor.</p>
<p>1.4. "Covered Software"
    means Source Code Form to which the initial Contributor has attached
    the notice in Exhibit A, the Executable Form of such Source Code
    Form, and Modifications of such Source Code Form, in each case
    including portions thereof.</p>
<p>1.5. "Incompatible With Secondary Licenses"
    means</p>
<pre><code>(a) that the initial Contributor has attached the notice described
    in Exhibit B to the Covered Software; or

(b) that the Covered Software was made available under the terms of
    version 1.1 or earlier of the License, but not also under the
    terms of a Secondary License.
</code></pre>
<p>1.6. "Executable Form"
    means any form of the work other than Source Code Form.</p>
<p>1.7. "Larger Work"
    means a work that combines Covered Software with other material, in
    a separate file or files, that is not Covered Software.</p>
<p>1.8. "License"
    means this document.</p>
<p>1.9. "Licensable"
    means having the right to grant, to the maximum extent possible,
    whether at the time of the initial grant or subsequently, any and
    all of the rights conveyed by this License.</p>
<p>1.10. "Modifications"
    means any of the following:</p>
<pre><code>(a) any file in Source Code Form that results from an addition to,
    deletion from, or modification of the contents of Covered
    Software; or

(b) any new file in Source Code Form that contains any Covered
    Software.
</code></pre>
<p>1.11. "Patent Claims" of a Contributor
    means any patent claim(s), including without limitation, method,
    process, and apparatus claims, in any patent Licensable by such
    Contributor that would be infringed, but for the grant of the
    License, by the making, using, selling, offering for sale, having
    made, import, or transfer of either its Contributions or its
    Contributor Version.</p>
<p>1.12. "Secondary License"
    means either the GNU General Public License, Version 2.0, the GNU
    Lesser General Public License, Version 2.1, the GNU Affero General
    Public License, Version 3.0, or any later versions of those
    licenses.</p>
<p>1.13. "Source Code Form"
    means the form of the work preferred for making modifications.</p>
<p>1.14. "You" (or "Your")
    means an individual or a legal entity exercising rights under this
    License. For legal entities, "You" includes any entity that
    controls, is controlled by, or is under common control with You. For
    purposes of this definition, "control" means (a) the power, direct
    or indirect, to cause the direction or management of such entity,
    whether by contract or otherwise, or (b) ownership of more than
    fifty percent (50%) of the outstanding shares or beneficial
    ownership of such entity.</p>
<h3 id="2licensegrantsandconditions">2. License Grants and Conditions</h3>
<p>2.1. Grants</p>
<p>Each Contributor hereby grants You a world-wide, royalty-free,
non-exclusive license:</p>
<p>(a) under intellectual property rights (other than patent or trademark)
    Licensable by such Contributor to use, reproduce, make available,
    modify, display, perform, distribute, and otherwise exploit its
    Contributions, either on an unmodified basis, with Modifications, or
    as part of a Larger Work; and</p>
<p>(b) under Patent Claims of such Contributor to make, use, sell, offer
    for sale, have made, import, and otherwise transfer either its
    Contributions or its Contributor Version.</p>
<p>2.2. Effective Date</p>
<p>The licenses granted in Section 2.1 with respect to any Contribution
become effective for each Contribution on the date the Contributor first
distributes such Contribution.</p>
<p>2.3. Limitations on Grant Scope</p>
<p>The licenses granted in this Section 2 are the only rights granted under
this License. No additional rights or licenses will be implied from the
distribution or licensing of Covered Software under this License.
Notwithstanding Section 2.1(b) above, no patent license is granted by a
Contributor:</p>
<p>(a) for any code that a Contributor has removed from Covered Software;
    or</p>
<p>(b) for infringements caused by: (i) Your and any other third party's
    modifications of Covered Software, or (ii) the combination of its
    Contributions with other software (except as part of its Contributor
    Version); or</p>
<p>(c) under Patent Claims infringed by Covered Software in the absence of
    its Contributions.</p>
<p>This License does not grant any rights in the trademarks, service marks,
or logos of any Contributor (except as may be necessary to comply with
the notice requirements in Section 3.4).</p>
<p>2.4. Subsequent Licenses</p>
<p>No Contributor makes additional grants as a result of Your choice to
distribute the Covered Software under a subsequent version of this
License (see Section 10.2) or under the terms of a Secondary License (if
permitted under the terms of Section 3.3).</p>
<p>2.5. Representation</p>
<p>Each Contributor represents that the Contributor believes its
Contributions are its original creation(s) or it has sufficient rights
to grant the rights to its Contributions conveyed by this License.</p>
<p>2.6. Fair Use</p>
<p>This License is not intended to limit any rights You have under
applicable copyright doctrines of fair use, fair dealing, or other
equivalents.</p>
<p>2.7. Conditions</p>
<p>Sections 3.1, 3.2, 3.3, and 3.4 are conditions of the licenses granted
in Section 2.1.</p>
<h3 id="3responsibilities">3. Responsibilities</h3>
<p>3.1. Distribution of Source Form</p>
<p>All distribution of Covered Software in Source Code Form, including any
Modifications that You create or to which You contribute, must be under
the terms of this License. You must inform recipients that the Source
Code Form of the Covered Software is governed by the terms of this
License, and how they can obtain a copy of this License. You may not
attempt to alter or restrict the recipients' rights in the Source Code
Form.</p>
<p>3.2. Distribution of Executable Form</p>
<p>If You distribute Covered Software in Executable Form then:</p>
<p>(a) such Covered Software must also be made available in Source Code
    Form, as described in Section 3.1, and You must inform recipients of
    the Executable Form how they can obtain a copy of such Source Code
    Form by reasonable means in a timely manner, at a charge no more
    than the cost of distribution to the recipient; and</p>
<p>(b) You may distribute such Executable Form under the terms of this
    License, or sublicense it under different terms, provided that the
    license for the Executable Form does not attempt to limit or alter
    the recipients' rights in the Source Code Form under this License.</p>
<p>3.3. Distribution of a Larger Work</p>
<p>You may create and distribute a Larger Work under terms of Your choice,
provided that You also comply with the requirements of this License for
the Covered Software. If the Larger Work is a combination of Covered
Software with a work governed by one or more Secondary Licenses, and the
Covered Software is not Incompatible With Secondary Licenses, this
License permits You to additionally distribute such Covered Software
under the terms of such Secondary License(s), so that the recipient of
the Larger Work may, at their option, further distribute the Covered
Software under the terms of either this License or such Secondary
License(s).</p>
<p>3.4. Notices</p>
<p>You may not remove or alter the substance of any license notices
(including copyright notices, patent notices, disclaimers of warranty,
or limitations of liability) contained within the Source Code Form of
the Covered Software, except that You may alter any license notices to
the extent required to remedy known factual inaccuracies.</p>
<p>3.5. Application of Additional Terms</p>
<p>You may choose to offer, and to charge a fee for, warranty, support,
indemnity or liability obligations to one or more recipients of Covered
Software. However, You may do so only on Your own behalf, and not on
behalf of any Contributor. You must make it absolutely clear that any
such warranty, support, indemnity, or liability obligation is offered by
You alone, and You hereby agree to indemnify every Contributor for any
liability incurred by such Contributor as a result of warranty, support,
indemnity or liability terms You offer. You may include additional
disclaimers of warranty and limitations of liability specific to any
jurisdiction.</p>
<h3 id="4inabilitytocomplyduetostatuteorregulation">4. Inability to Comply Due to Statute or Regulation</h3>
<p>If it is impossible for You to comply with any of the terms of this
License with respect to some or all of the Covered Software due to
statute, judicial order, or regulation then You must: (a) comply with
the terms of this License to the maximum extent possible; and (b)
describe the limitations and the code they affect. Such description must
be placed in a text file included with all distributions of the Covered
Software under this License. Except to the extent prohibited by statute
or regulation, such description must be sufficiently detailed for a
recipient of ordinary skill to be able to understand it.</p>
<h3 id="5termination">5. Termination</h3>
<p>5.1. The rights granted under this License will terminate automatically
if You fail to comply with any of its terms. However, if You become
compliant, then the rights granted under this License from a particular
Contributor are reinstated (a) provisionally, unless and until such
Contributor explicitly and finally terminates Your grants, and (b) on an
ongoing basis, if such Contributor fails to notify You of the
non-compliance by some reasonable means prior to 60 days after You have
come back into compliance. Moreover, Your grants from a particular
Contributor are reinstated on an ongoing basis if such Contributor
notifies You of the non-compliance by some reasonable means, this is the
first time You have received notice of non-compliance with this License
from such Contributor, and You become compliant prior to 30 days after
Your receipt of the notice.</p>
<p>5.2. If You initiate litigation against any entity by asserting a patent
infringement claim (excluding declaratory judgment actions,
counter-claims, and cross-claims) alleging that a Contributor Version
directly or indirectly infringes any patent, then the rights granted to
You by any and all Contributors for the Covered Software under Section
2.1 of this License shall terminate.</p>
<p>5.3. In the event of termination under Sections 5.1 or 5.2 above, all
end user license agreements (excluding distributors and resellers) which
have been validly granted by You or Your distributors under this License
prior to termination shall survive termination.</p>
<hr />
<ul>
<li>*</li>
<li>6. Disclaimer of Warranty                                           *</li>
<li>-------------------------                                           *</li>
<li>*</li>
<li>Covered Software is provided under this License on an "as is"       *</li>
<li>basis, without warranty of any kind, either expressed, implied, or  *</li>
<li>statutory, including, without limitation, warranties that the       *</li>
<li>Covered Software is free of defects, merchantable, fit for a        *</li>
<li>particular purpose or non-infringing. The entire risk as to the     *</li>
<li>quality and performance of the Covered Software is with You.        *</li>
<li>Should any Covered Software prove defective in any respect, You     *</li>
<li>(not any Contributor) assume the cost of any necessary servicing,   *</li>
<li>repair, or correction. This disclaimer of warranty constitutes an   *</li>
<li>essential part of this License. No use of any Covered Software is   *</li>
<li>authorized under this License except under this disclaimer.         *</li>
<li>*</li>
</ul>
<hr />
<hr />
<ul>
<li>*</li>
<li>7. Limitation of Liability                                          *</li>
<li>--------------------------                                          *</li>
<li>*</li>
<li>Under no circumstances and under no legal theory, whether tort      *</li>
<li>(including negligence), contract, or otherwise, shall any           *</li>
<li>Contributor, or anyone who distributes Covered Software as          *</li>
<li>permitted above, be liable to You for any direct, indirect,         *</li>
<li>special, incidental, or consequential damages of any character      *</li>
<li>including, without limitation, damages for lost profits, loss of    *</li>
<li>goodwill, work stoppage, computer failure or malfunction, or any    *</li>
<li>and all other commercial damages or losses, even if such party      *</li>
<li>shall have been informed of the possibility of such damages. This   *</li>
<li>limitation of liability shall not apply to liability for death or   *</li>
<li>personal injury resulting from such party's negligence to the       *</li>
<li>extent applicable law prohibits such limitation. Some               *</li>
<li>jurisdictions do not allow the exclusion or limitation of           *</li>
<li>incidental or consequential damages, so this exclusion and          *</li>
<li>limitation may not apply to You.                                    *</li>
<li>*</li>
</ul>
<hr />
<h3 id="8litigation">8. Litigation</h3>
<p>Any litigation relating to this License may be brought only in the
courts of a jurisdiction where the defendant maintains its principal
place of business and such litigation shall be governed by laws of that
jurisdiction, without reference to its conflict-of-law provisions.
Nothing in this Section shall prevent a party's ability to bring
cross-claims or counter-claims.</p>
<h3 id="9miscellaneous">9. Miscellaneous</h3>
<p>This License represents the complete agreement concerning the subject
matter hereof. If any provision of this License is held to be
unenforceable, such provision shall be reformed only to the extent
necessary to make it enforceable. Any law or regulation which provides
that the language of a contract shall be construed against the drafter
shall not be used to construe this License against a Contributor.</p>
<h3 id="10versionsofthelicense">10. Versions of the License</h3>
<p>10.1. New Versions</p>
<p>Mozilla Foundation is the license steward. Except as provided in Section
10.3, no one other than the license steward has the right to modify or
publish new versions of this License. Each version will be given a
distinguishing version number.</p>
<p>10.2. Effect of New Versions</p>
<p>You may distribute the Covered Software under the terms of the version
of the License under which You originally received the Covered Software,
or under the terms of any subsequent version published by the license
steward.</p>
<p>10.3. Modified Versions</p>
<p>If you create software not governed by this License, and you want to
create a new license for such software, you may create and use a
modified version of this License if you rename the license and remove
any references to the name of the license steward (except to note that
such modified license differs from this License).</p>
<p>10.4. Distributing Source Code Form that is Incompatible With Secondary
Licenses</p>
<p>If You choose to distribute Source Code Form that is Incompatible With
Secondary Licenses under the terms of this version of the License, the
notice described in Exhibit B of this License must be attached.</p>
<h3 id="exhibitasourcecodeformlicensenotice">Exhibit A - Source Code Form License Notice</h3>
<p>This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at <a href="http://mozilla.org/MPL/2.0/." target="_blank">http://mozilla.org/MPL/2.0/.</a></p>
<p>If it is not possible or desirable to put the notice in a particular
file, then You may include the notice in a location (such as a LICENSE
file in a relevant directory) where a recipient would be likely to look
for such a notice.</p>
<p>You may add additional accurate notices of copyright ownership.</p>
<h3 id="exhibitbincompatiblewithsecondarylicensesnotice">Exhibit B - "Incompatible With Secondary Licenses" Notice</h3>
<p>This Source Code Form is "Incompatible With Secondary Licenses", as
  defined by the Mozilla Public License, v. 2.0.</p>'''