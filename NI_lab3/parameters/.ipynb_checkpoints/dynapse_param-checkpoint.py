#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This dictionary contains the default parameters for the
Differential Pair Integrator (DPI) neuron including synapses as implemented on
the DYNAP-SE chip, developed at the Institute of Neuroinformatic.
Circuit and equations were published in Chicca et al. 2014
These values were estimated empircally based on the example in the tutorial.
These parameters may serve you as a starting point for a given experiment.
"""

from brian2 import pF, ms, pA, nA
from parameters import constants


dynapse_param = {
    "kn": constants.kappa_n,            # Subthreshold slope factor, do not change
    "kp": constants.kappa_p,            # Subthreshold slope factor, do not change
    "Ut": constants.Ut,                 # Thermal voltage, do not change
    "Io": constants.Io,                 # Dark current, can be from 2x to 10x default Io if necessary
    "Cmem": 1.5 * pF,                   # Membrane capacitance, fixed at layout time (see chip for details)
    "Ispkthr": 1. * nA,                 # Spiking threshold current, depends on layout (see chip for details)
    "refP": 1. * ms,                    # Refractory period, limits maximum firing rate
    "Ireset": 0.6 * pA,                 # Reset current after spike generation
    "Iconst": constants.Io,             # Initialize constant current injection to Io
    ##################
    "Itau": 8. * pA,                    # Membrane time constant current, the time constant is inversely proportional to Itau
    "Ishunt": constants.Io,             # Initialize shunting inhibitory current to Io
    "Ith": 0.9 * pA,                    # Threshold / gain current, scaling factor for the membrane current (typically equal to Itau)
    #  ADAPTATION  ######################
    "Ica": 2. * pA,                     # Spike-frequency adaptation weight current
    "Itauahp": 1 * pA,                  # Spike-frequency adaptation time constant current
    "Ithahp": 1 * pA,                   # Spike-frequency adaptation threshold
    "Cahp": 1 * pF,                     # Spike-frequency adaptation capacitance
    "Iahp": constants.Io,               # Initialize spike-frequency adaptation output current to Io
    #  POSTIVE FEEDBACK #################
    "Iath": 0.5 * nA,                   # Feedback threshold current, typically a fraction of Ispkthr
    "Iagain": 50. * pA,                 # Feedback gain current, heuristic parameter
    "Ianorm": 10. * pA,                 # Feedback normalization current, heuristic parameter
    # Synapse parameters ################
    #exc
    'C_syn_exc': 1.5 * pF,               # Syanptic capacitance, fixed at layout time (see chip for details)
    'I_tau_syn_exc': 10. * pA,           # Synapctic time constant current, the time constant is inversely proportional to I_tau
    'I_wo_syn_exc': 50. * pA,            # Base synaptic weight current which can be scaled by the .weight parameter
    'I_th_syn_exc': 10. * pA,            # DPI's threshold / gain current, scaling factor for the synaptic weight (typically equal to I_tau)
    'I_syn_exc': constants.Io,           # Output current initial value
    #exc2
    'C_syn_exc2': 1.5 * pF,               # Syanptic capacitance, fixed at layout time (see chip for details)
    'I_tau_syn_exc2': 10. * pA,           # Synapctic time constant current, the time constant is inversely proportional to I_tau
    'I_wo_syn_exc2': 50. * pA,            # Base synaptic weight current which can be scaled by the .weight parameter
    'I_th_syn_exc2': 10. * pA,            # DPI's threshold / gain current, scaling factor for the synaptic weight (typically equal to I_tau)
    'I_syn_exc2': constants.Io,           # Output current initial value
    #inh
    'C_syn_inh': 1.5 * pF,               # Syanptic capacitance, fixed at layout time (see chip for details)
    'I_tau_syn_inh': 10. * pA,           # Synapctic time constant current, the time constant is inversely proportional to I_tau
    'I_wo_syn_inh': 50. * pA,            # Base synaptic weight current which can be scaled by the .weight parameter
    'I_th_syn_inh': 10. * pA,            # DPI's threshold / gain current, scaling factor for the synaptic weight (typically equal to I_tau)
    'I_syn_inh': constants.Io,           # Output current initial value
    #shunt
    'C_syn_shunt': 1.5 * pF,             # Syanptic capacitance, fixed at layout time (see chip for details)
    'I_tau_syn_shunt': 10. * pA,         # Synapctic time constant current, the time constant is inversely proportional to I_tau
    'I_wo_syn_shunt': 50. * pA,          # Base synaptic weight current which can be scaled by the .weight parameter
    'I_th_syn_shunt': 10. * pA,          # DPI's threshold / gain current, scaling factor for the synaptic weight (typically equal to I_tau)
    'I_syn_shunt': constants.Io          # Output current initial value
}