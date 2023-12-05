import pylse

def print_events_trace(events, signal_list, until, resolution=10, max_char=15):
    # Print out a text chart of all the events in the signal list
    # Input: events - PyLSE events dictionary
    #       signal_list - list of signal names to inspect
    #       until - time to stop printing events
    #       resolution - time resolution of the printed chart (picoseconds)
    #       max_char - maximum number of characters to print for each signal name

    print("Printing events:")
    # For each signal
    for signal in signal_list:
        # Print out the signal name
        # print out maximum of 10 characters for the signal name
        # pad missing spaces with _ characters
        signal_name = signal
        if len(signal_name) > max_char:
            signal_name = signal_name[:max_char]
        else:
            signal_name = signal_name.ljust(max_char, "_")
        print(signal_name, end=":")

        # Check if this signal_name exists
        try:
            events[signal]
        except KeyError:
            print("Signal " + signal + " does not exist")
            continue

        # Print out whether there is an event or not at each time step
        for i in range(until//resolution):
            # Check whether there is an event at this time step within the resolution
            pulse_found = False
            for event in events[signal]:
                if i*resolution <= event < (i+1)*resolution:
                    print("X", end="")
                    pulse_found = True
                    break
            
            if not pulse_found:
                print("_", end="")
        
        print(":" + signal_name)

