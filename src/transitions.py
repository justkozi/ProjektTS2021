from statemachine import Transition


def setTransition(form, states, prefix):
    transitions = {}

    for indices in form:
        from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
        for to_idx in to_idx_tuple:  # iterate over destinations from a source state
            op_identifier = "{}_{}_{}".format(prefix, from_idx, to_idx)  # parametrize identifier of a transition

            # create transition object and add it to the transitions dict
            transition = Transition(states[from_idx], states[to_idx],
                                    identifier=op_identifier)
            transitions[op_identifier] = transition

            # add transition to source state
            states[from_idx].transitions.append(transition)
    return states, transitions
