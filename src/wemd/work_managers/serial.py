from __future__ import division; __metaclass__ = type

import numpy, math, logging

log = logging.getLogger(__name__)

from wemd.work_managers import WEMDWorkManager

# This is mostly for demonstration; serious parallelism probably needs processes, so that the
# global interpreter lock doesn't get in the way.

class SerialWorkManager(WEMDWorkManager):
    def __init__(self, sim_manager):
        log.debug('initializing threaded work manager')
        super(SerialWorkManager,self).__init__(sim_manager)
        self.n_iter = None        
        self.block_size = 1
        
    def propagate_particles(self, segments):
        propagator = self.sim_manager.propagator
        system_driver = self.sim_manager.system
        for segment in segments:
            propagator.prepare_segment(segment)
            system_driver.preprocess_segment(segment)
            propagator.propagate_segments([segment])
            system_driver.postprocess_segment(segment)
            propagator.finalize_segment(segment)
