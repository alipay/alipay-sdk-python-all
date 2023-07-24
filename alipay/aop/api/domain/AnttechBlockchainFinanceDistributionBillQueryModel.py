#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceDistributionBillQueryModel(object):

    def __init__(self):
        self._distribution_order_id = None
        self._distribution_pro_no = None
        self._write_off_biz_no = None

    @property
    def distribution_order_id(self):
        return self._distribution_order_id

    @distribution_order_id.setter
    def distribution_order_id(self, value):
        self._distribution_order_id = value
    @property
    def distribution_pro_no(self):
        return self._distribution_pro_no

    @distribution_pro_no.setter
    def distribution_pro_no(self, value):
        self._distribution_pro_no = value
    @property
    def write_off_biz_no(self):
        return self._write_off_biz_no

    @write_off_biz_no.setter
    def write_off_biz_no(self, value):
        self._write_off_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.distribution_order_id:
            if hasattr(self.distribution_order_id, 'to_alipay_dict'):
                params['distribution_order_id'] = self.distribution_order_id.to_alipay_dict()
            else:
                params['distribution_order_id'] = self.distribution_order_id
        if self.distribution_pro_no:
            if hasattr(self.distribution_pro_no, 'to_alipay_dict'):
                params['distribution_pro_no'] = self.distribution_pro_no.to_alipay_dict()
            else:
                params['distribution_pro_no'] = self.distribution_pro_no
        if self.write_off_biz_no:
            if hasattr(self.write_off_biz_no, 'to_alipay_dict'):
                params['write_off_biz_no'] = self.write_off_biz_no.to_alipay_dict()
            else:
                params['write_off_biz_no'] = self.write_off_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceDistributionBillQueryModel()
        if 'distribution_order_id' in d:
            o.distribution_order_id = d['distribution_order_id']
        if 'distribution_pro_no' in d:
            o.distribution_pro_no = d['distribution_pro_no']
        if 'write_off_biz_no' in d:
            o.write_off_biz_no = d['write_off_biz_no']
        return o


