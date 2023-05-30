#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceFsupvTransferQueryModel(object):

    def __init__(self):
        self._accepted_no = None

    @property
    def accepted_no(self):
        return self._accepted_no

    @accepted_no.setter
    def accepted_no(self, value):
        self._accepted_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.accepted_no:
            if hasattr(self.accepted_no, 'to_alipay_dict'):
                params['accepted_no'] = self.accepted_no.to_alipay_dict()
            else:
                params['accepted_no'] = self.accepted_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceFsupvTransferQueryModel()
        if 'accepted_no' in d:
            o.accepted_no = d['accepted_no']
        return o


