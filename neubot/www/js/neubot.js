/* neubot/www/js/neubot.js */
/*-
 * Copyright (c) 2010 Antonio Servetti <antonio.servetti@polito.it>,
 *  Politecnico di Torino
 *
 * Copyright (c) 2010 Simone Basso <bassosimone@gmail.com>,
 *  NEXA Center for Internet & Society at Politecnico di Torino
 *
 * This file is part of Neubot <http://www.neubot.org/>.
 *
 * Neubot is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Neubot is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Neubot.  If not, see <http://www.gnu.org/licenses/>.
 */

/*
 * For results.html we have js/results.js, therefore it might
 * make sense to rename this file js/index.js for consistency.
 * OTOH js/index.js seems odd to me.
 * Update: Alessio pointed out that usually you put all the
 * javascript magic into a single file so the browser does
 * not need to load new stuff when you switch page, and that's
 * probably the way to go, i.e. to merge everything we need
 * here in this file.
 */

(function() {

    var prevStatus;

    function process_state(data) {
        var current;
        var value;
        var func;
        var attr;
        var prev;

        // Reset style

        $('table#state tr').css('font-weight', 'normal');
        $('#testResultsBox h4').text("Latest test details");
        $('#next_rendezvous').text("");
        $("#queueInfo").text("");

        // Keep processing simple to read and understand:
        // consider each relevant tag on its own but delay
        // the show / hide decisions

        value = neubot.XML_number("pid", data);
        if (value != "")
            $("#pid").text(value);

        value = neubot.XML_timestamp("next_rendezvous", data);
        if (value != "") {
            value = value - neubot.unix_time();
            // The sysadmin might have adjusted the clock
            if (value >= 0) {
                value = neubot.timestamp_to_minutes(value);
                value = neubot.format_minutes(value);
                $("#next_rendezvous").text(value);
            }
        }

        value = neubot.XML_timestamp("since", data);
        if (value != "") {
            value = neubot.timestamp_to_date(value);
            value = neubot.format_date(value);
            $("#since").text(value);
        }

        value = neubot.XML_text("update", data);
        if (value != "") {
            $("#updateUrl").text($("update", data).attr("uri"));
            $("#updateVersion").text(value);
            $("#update").show();
        } else {
            $("#update").hide();
        }

        value = neubot.XML_text("negotiate queuePos", data);
        if (value != "")
            $("#queuePos").text(value);
        value = neubot.XML_text("negotiate queueLen", data);
        if (value != "")
            $("#queueLen").text(value);

        value = neubot.XML_timestamp("test timestamp", data);
        if (value != "") {
            value = neubot.timestamp_to_date(value);
            value = neubot.format_date(value);
            $("#testTime").text(value);
        }
        value = neubot.XML_text("test name", data);
        if (value != "") {
            // XXX XXX XXX This is sooo ugly!
            $("#testName").text(value);
            $("#testName1").text(value);
        }
        // Be prepared to support other test types
        if (value == "speedtest") {
            value = neubot.XML_text('test result[tag="latency"]', data);
            if (value != "")
                $("#latencyResult").text(value);
            value = neubot.XML_text('test result[tag="download"]', data);
            if (value != "")
                $("#downloadResult").text(value);
            value = neubot.XML_text('test result[tag="upload"]', data);
            if (value != "")
                $("#uploadResult").text(value);
        }

        // Get the current and the previous statuses
        // Use 'idle' as current state if we are inactive
        // Those are needed to take decisions below

        current = neubot.XML_text('activity[current="true"]', data);
        if (current == "")
            current = "idle";
        prev = prevStatus
        prevStatus = current

        // We must update the results plot after a test
        // but we must be careful because 'collect' is one
        // of the most transient states, therefore be
        // paranoid and issue a robust check

        // Not yet
        /*
        if (prev != "idle" && (current == "negotiate" || current == "idle"))
            neubot.update_results_plot();
        */

        // Adjust style
        // The qtip must be visible while we are testing
        // and must not be visible otherwise

        if (current == "test" && prev != "test") {
            $('#latencyResult').text("---");
            $('#uploadResult').text("---");
            $('#downloadResult').text("---");
            $('#testResultsBox').qtip("show");
        }
        if (current == "idle")                  // XXX
            $('#testResultsBox').qtip("hide");
        if (current == "test")
            $('#testResultsBox h4').text("Current test details");

        $('table#state tr#' + current).css('font-weight', 'bold');
    }

    $(document).ready(function() {
        $.jqplot.config.enablePlugins = true;

        $('#testResultsBox').qtip({
            content: "A new test is running.",
            position: {
                target: $('#testTime'),
                corner: {
                    tooltip: "rightMiddle",
                    target: "leftMiddle"
                }
            },
            show: {
                when: false,
                ready: false
            },
            hide: false,
            style: {
                border: {
                    width: 2,
                    radius: 5
                },
                padding: 10,
                textAlign: 'center',
                tip: true,
                name: 'blue'
            }
        });

        // Not yet
        /*
        neubot.update_results_plot(500);
        */

        tracker = neubot.state_tracker(process_state);
        tracker.start();
    });

})();
