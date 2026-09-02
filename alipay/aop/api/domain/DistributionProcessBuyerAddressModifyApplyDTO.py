#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DistributionProcessBuyerAddressModifyApplyDTO(object):

    def __init__(self):
        self._agree = None

    @property
    def agree(self):
        return self._agree

    @agree.setter
    def agree(self, value):
        self._agree = value


    def to_alipay_dict(self):
        params = dict()
        if self.agree:
            if hasattr(self.agree, 'to_alipay_dict'):
                params['agree'] = self.agree.to_alipay_dict()
            else:
                params['agree'] = self.agree
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DistributionProcessBuyerAddressModifyApplyDTO()
        if 'agree' in d:
            o.agree = d['agree']
        return o


