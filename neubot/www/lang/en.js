// neubot/www/lang/en.js

//
// Copyright (c) 2011 Simone Basso <bassosimone@gmail.com>,
//  NEXA Center for Internet & Society at Politecnico di Torino
//
// This file is part of Neubot <http://www.neubot.org/>.
//
// Neubot is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Neubot is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Neubot.  If not, see <http://www.gnu.org/licenses/>.
//

//
// WARNING! Autogenerated file: don't edit
// Use './scripts/make_lang_en.py' instead to regenerate it
// Created: Thu, 08 Sep 2011 06:25:29 GMT
//

var LANG = {
    'Current test results': 'Current test results',

    'Disable': 'Disable',

    'Enable': 'Enable',

    'Latest test results': 'Latest test results',

    'Test running': 'Test running',

    'Your bittorrent download and upload speed': 'Your bittorrent download and upload speed',

    'Your download and upload speed': 'Your download and upload speed',

    'disabled': 'disabled',

    'enabled': 'enabled',

    'i18n_about': 'About',

    'i18n_about_text':
'This is the web user interface of Neubot v0.4.2-rc5.\
 Neubot is a lightweight <a href="http://www.neubot.org/copying">open-source</a> program\
 that runs in background and periodically performs\
 transmission tests to probe your Internet connection\
 using various application level protocols. <a href="http://www.neubot.org/faq">Read more</a>',

    'i18n_bittorrent': 'Bittorrent',

    'i18n_bittorrent_explanation':
'This tests downloads and uploads a given number of bytes from\
 a remote server using the BitTorrent protocol. It reports the\
 average download and upload speed measured during the test as\
 well as the time required to connect to the remote server,\
 which approximates the round-trip time latency.',

    'i18n_bittorrent_explanation_2':
'Please, note that this test is quite different from the speedtest\
 one, so there are cases where the comparison between the two is not\
 feasible. We\'re working to deploy an HTTP test that mimics the\
 behavior of this one, so that it\'s always possible to compare them.',

    'i18n_bittorrent_see_last': 'View last',

    'i18n_bittorrent_see_last_days': 'day',

    'i18n_bittorrent_see_last_hours': 'hour',

    'i18n_bittorrent_title': 'Your recent bittorrent results',

    'i18n_collect_status_text':
'The daemon is uploading the results of the latest\
 transmission test to the neubot project servers.',

    'i18n_current_status': 'Current Neubot status',

    'i18n_description': 'Description',

    'i18n_dlspeed': 'Download speed',

    'i18n_footer_text':
'Neubot is a research project on network neutrality of the<br/>\
 <a href="http://nexa.polito.it/">NEXA Center for Internet &amp;\
 Society</a> at <a href="http://www.dauin.polito.it/">Politecnico\
 di Torino</a>.',

    'i18n_header_subtitle': 'The web-interface to control the neubot daemon',

    'i18n_header_title': '<a href="index.html">Neubot web interface</a>',

    'i18n_idle_status_text':
'The daemon is sleeping. The next rendezvous will\
 start in <em><span id="next_rendezvous">(information\
 not available)</span></em>.',

    'i18n_infonav': '(n/a)',

    'i18n_latency': 'Latency',

    'i18n_latest': 'Latest test details',

    'i18n_log': 'Log',

    'i18n_negotiate_status_text':
'The daemon is waiting for its turn to perform a\
 transmission test. The last known position in queue\
 is <em><span id="queuePos">(no negotiations\
 yet)</span></em>.',

    'i18n_neubotis': 'Neubot is',

    'i18n_privacy': 'Privacy',

    'i18n_privacy_explanation':
'In this page we spell out the details of our <a href="#policy">privacy policy</a>, in order to comply with\
 European law. And we provide a simple <a href="#dashboard">privacy\
 dashboard</a> to manage the permissions you give us with\
 respect to the treatment of your Internet address, which\
 is personal data in EU.',

    'i18n_privacy_policy':
'\n\
    $Version: 1.0$\n\
\n\
    The purpose of Neubot is to measure the quality and neutrality of\n\
    your Internet connection and to share the results with the Internet\n\
    community, in order to rebalance the information asymmetry between\n\
    ordinary Internet users and Service Providers.\n\
\n\
    Neubot does not monitor or analyze your Internet traffic. It just\n\
    uses a tiny fraction of your connection capacity to perform background\n\
    transmission tests, sending and/or receiving random data.  The\n\
    result contains the measured performance metrics, such as the\n\
    download speed, or the latency, as well as your computer load, as\n\
    a percentage.  Also, the result contains your Internet address.\n\
    After the test, the result is uploaded to Neubot servers.\n\
\n\
    The Neubot project needs to collect your Internet address because\n\
    that allows to infer your Internet Service Provider and to have a\n\
    rough idea of your location.  This is paramount for Neubot\'s\n\
    goal of monitoring the quality and neutrality of the Internet, by\n\
    provider and geographical area.\n\
\n\
    However, in Europe Internet addresses are personal data. So, Neubot\n\
    cannot store, process, or share your Internet address without your\n\
    prior *informed consent*, under the provisions of the &quot;Codice in\n\
    materia di protezione dei dati personali&quot; `(Decree 196/03)\n\
    &lt;http://www.garanteprivacy.it/garante/doc.jsp?ID=1311248&gt;`_.  In\n\
    accordance with the law, data controller is the NEXA Center for\n\
    Internet &amp; Society, represented by its co-director Juan Carlos\n\
    De Martin.\n\
\n\
    Neubot asks you to explicitly assert that you have read this privacy\n\
    policy and to give it the permission to collect and share your IP\n\
    address.  If you don\'t confirm that you have read the privacy policy,\n\
    Neubot collects your Internet address under a special provision,\n\
    that allows researchers to do that `for statistical purposes only\n\
    &lt;http://www.garanteprivacy.it/garante/doc.jsp?ID=1556635&gt;`_.  Internet\n\
    addresses collected under this regime will be flagged in a special\n\
    way, and will not be shared with anyone.  They will be treated by\n\
    the researchers authorized by the data controller only.  This data,\n\
    however, will not be of great value for the Internet community,\n\
    because they cannot be shared with and analyzed by other researchers.\n\
\n\
    The project needs at least the permission to collect your Internet\n\
    address, because otherwise it cannot process your results and publish\n\
    aggregate data.  If you don\'t give Neubot the permission to share,\n\
    of course your Internet address will not be shared with others, and\n\
    will be processed by the researchers authorized by the data controller\n\
    only.  Please note that there is a great benefit in sharing your\n\
    Internet address, because that allows other researchers to study\n\
    and criticize Neubot methodology and data set.  This will empower\n\
    the Internet community, eventually leading to a better understanding\n\
    of the Net.\n\
\n\
    The data controller guarantees you the rights as per Section 7 of\n\
    the above mentioned decree.  Basically, you have total control over\n\
    you personal data, and you can, for example, inquire Neubot to\n\
    remove your Internet address from its data sets.  To exercise your\n\
    rights, please write to Dipartimento di Automatica e Infomatica\n\
    (DAUIN) - Politecnico di Torino - Corso Duca degli Abruzzi, 24 -\n\
    10129 Torino, ITALY.\n\
        ',

    'i18n_privacy_settings_1': 'This is the current state of your privacy settings:',

    'i18n_privacy_settings_2':
'<input id="check_privacy_informed" type="checkbox" value="0"/><label class="i18n i18n_privacy_settings_2_informed" for="check_privacy_informed"><b>Informed</b> You assert that you\
 have read and understood the above privacy policy</label>\
 <br/>\
 <input id="check_privacy_can_collect" type="checkbox" value="0"/><label class="i18n i18n_privacy_settings_2_can_collect" for="check_privacy_can_collect"><b>Can collect</b> You give Neubot\
 the permission to collect your Internet address</label>\
 <br/>\
\
 <input id="check_privacy_can_share" type="checkbox" value="0"/><label class="i18n i18n_privacy_settings_2_can_share" for="check_privacy_can_share"><b>Can share</b> You give Neubot the\
 permission to share your Internet address with the Internet\
 community</label>\
 <br/>',

    'i18n_privacy_title_1': 'Privacy policy',

    'i18n_privacy_title_2': 'Privacy dashboard',

    'i18n_privacy_warning':
'If you don\'t assert that you are <em>Informed</em>, your Internet\
 address will be treated under the special provisions for statistical\
 purposes only, as explained above. You can decide whether Neubot\
 <em>can collect</em> and <em>can share</em> only if you acknowledge\
 that you are <em>informed</em>.',

    'i18n_rendezvous_status_text':
'The daemon is connecting to the <em>master server</em>\
 and retrieves test instructions and update information.',

    'i18n_resultof': 'Result of',

    'i18n_settings': 'Settings',

    'i18n_settings_par1':
'In this page we list all the knobs you can twist,\
 including obscure and dangerous settings.\
 Please, make sure you understand what you are doing\
 before making any change. You\'re on your own if\
 something breaks because of your changes.',

    'i18n_settings_par2':
'Some settings, such as <code>agent.api.address</code>\
 and <code>agent.api.port</code>, are not effective\
 until you restart Neubot.',

    'i18n_settings_title': 'Settings',

    'i18n_speedtest': 'Speedtest',

    'i18n_speedtest_explanation_1':
'Speedtest is a test that sheds some light on the quality\
 of your broadband connection, by downloading/uploading random data\
 to/from a remote server, and reporting the average speeds. The\
 test also yields an over-estimate of the round-trip latency between\
 you and such remote server. For more information, see the\
<a href="http://www.neubot.org/faq#what-does-speedtest-test-measures">FAQ</a>.',

    'i18n_speedtest_explanation_2':
'To put the results of this test in the context of the\
 average broadband speed available in your country you\
 might want to check the statistics available at the <a href="http://www.oecd.org/sti/ict/broadband">OECD Broadband\
 Portal</a>. In particular, it might be interesting to read <a href="http://www.oecd.org/dataoecd/10/53/39575086.xls">&quot;Average\
 advertised download speeds, by country&quot;</a> (in XLS format).',

    'i18n_speedtest_see_last': 'View last',

    'i18n_speedtest_see_last_days': 'day',

    'i18n_speedtest_see_last_hours': 'hour',

    'i18n_speedtest_title': 'Your recent speedtest results',

    'i18n_state': 'State',

    'i18n_status': 'Status',

    'i18n_status_text':
'This is the web interface to control the <em>neubot daemon</em>,\
 that is running in background with pid <em>\
 <span id="pid">(information not available)</span></em> since\
 <em><span id="since">(information not available)</span></em>.\
 The following table provides some more details on the state of\
 the daemon and highlights the current state.',

    'i18n_test_status_text':
'The daemon is performing a transmission test. The\
 name of the test is <em><span id="testName">\
 (no tests yet)</span></em>.',

    'i18n_testnow': 'How do I run a test <em>now</em>?',

    'i18n_testnow_text':
'The support for starting a test <em>now</em> is not\
 yet implemented by this web user interface, but that is\
 in the TODO list. At the moment, the only way to run a\
 test <em>now</em> is to type the command <b><em>neubot\
 speedtest</em></b> into your favourite shell.',

    'i18n_ulspeed': 'Upload speed',

    'i18n_updavailable': 'Updates available',

    'i18n_website': 'Neubot web site',

    'i18n_welcome_text':
'Thank you for using Neubot! You are gaining some understanding\
 about your Internet Connection and helping the Internet Community\
 to understand what is going on in the network. This tab provides\
 a general overview of the status of the neubot daemon. Above there\
 are a number of tabs, one for each available transmission test.\
 Each tab provides more information on the test and allows you to\
 review your recent results.'

};
