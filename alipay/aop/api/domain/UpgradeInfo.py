#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UpgradeInfo(object):

    def __init__(self):
        self._upgrade_after = None
        self._upgrade_before = None
        self._upgrade_force = None
        self._upgrade_target = None

    @property
    def upgrade_after(self):
        return self._upgrade_after

    @upgrade_after.setter
    def upgrade_after(self, value):
        self._upgrade_after = value
    @property
    def upgrade_before(self):
        return self._upgrade_before

    @upgrade_before.setter
    def upgrade_before(self, value):
        self._upgrade_before = value
    @property
    def upgrade_force(self):
        return self._upgrade_force

    @upgrade_force.setter
    def upgrade_force(self, value):
        self._upgrade_force = value
    @property
    def upgrade_target(self):
        return self._upgrade_target

    @upgrade_target.setter
    def upgrade_target(self, value):
        self._upgrade_target = value


    def to_alipay_dict(self):
        params = dict()
        if self.upgrade_after:
            if hasattr(self.upgrade_after, 'to_alipay_dict'):
                params['upgrade_after'] = self.upgrade_after.to_alipay_dict()
            else:
                params['upgrade_after'] = self.upgrade_after
        if self.upgrade_before:
            if hasattr(self.upgrade_before, 'to_alipay_dict'):
                params['upgrade_before'] = self.upgrade_before.to_alipay_dict()
            else:
                params['upgrade_before'] = self.upgrade_before
        if self.upgrade_force:
            if hasattr(self.upgrade_force, 'to_alipay_dict'):
                params['upgrade_force'] = self.upgrade_force.to_alipay_dict()
            else:
                params['upgrade_force'] = self.upgrade_force
        if self.upgrade_target:
            if hasattr(self.upgrade_target, 'to_alipay_dict'):
                params['upgrade_target'] = self.upgrade_target.to_alipay_dict()
            else:
                params['upgrade_target'] = self.upgrade_target
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UpgradeInfo()
        if 'upgrade_after' in d:
            o.upgrade_after = d['upgrade_after']
        if 'upgrade_before' in d:
            o.upgrade_before = d['upgrade_before']
        if 'upgrade_force' in d:
            o.upgrade_force = d['upgrade_force']
        if 'upgrade_target' in d:
            o.upgrade_target = d['upgrade_target']
        return o


