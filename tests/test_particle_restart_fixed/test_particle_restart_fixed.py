#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.pardir)
from testing_harness import ParticleRestartTestHarness


if __name__ == '__main__':
    harness = ParticleRestartTestHarness('particle_7_928.*')
    harness.main()
