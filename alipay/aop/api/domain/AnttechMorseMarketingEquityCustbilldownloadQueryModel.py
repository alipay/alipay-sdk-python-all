#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingEquityCustbilldownloadQueryModel(object):

    def __init__(self):
        self._bill_application_id = None

    @property
    def bill_application_id(self):
        return self._bill_application_id

    @bill_application_id.setter
    def bill_application_id(self, value):
        self._bill_application_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_application_id:
            if hasattr(self.bill_application_id, 'to_alipay_dict'):
                params['bill_application_id'] = self.bill_application_id.to_alipay_dict()
            else:
                params['bill_application_id'] = self.bill_application_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseMarketingEquityCustbilldownloadQueryModel()
        if 'bill_application_id' in d:
            o.bill_application_id = d['bill_application_id']
        return o


