#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FxiaokeUpdateContractRequest(object):

    def __init__(self):
        self._negotiation_file = None
        self._negotiation_no = None

    @property
    def negotiation_file(self):
        return self._negotiation_file

    @negotiation_file.setter
    def negotiation_file(self, value):
        self._negotiation_file = value
    @property
    def negotiation_no(self):
        return self._negotiation_no

    @negotiation_no.setter
    def negotiation_no(self, value):
        self._negotiation_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.negotiation_file:
            if hasattr(self.negotiation_file, 'to_alipay_dict'):
                params['negotiation_file'] = self.negotiation_file.to_alipay_dict()
            else:
                params['negotiation_file'] = self.negotiation_file
        if self.negotiation_no:
            if hasattr(self.negotiation_no, 'to_alipay_dict'):
                params['negotiation_no'] = self.negotiation_no.to_alipay_dict()
            else:
                params['negotiation_no'] = self.negotiation_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FxiaokeUpdateContractRequest()
        if 'negotiation_file' in d:
            o.negotiation_file = d['negotiation_file']
        if 'negotiation_no' in d:
            o.negotiation_no = d['negotiation_no']
        return o


