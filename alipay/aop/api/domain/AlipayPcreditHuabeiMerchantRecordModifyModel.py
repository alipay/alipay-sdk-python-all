#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HbMerchantInfo import HbMerchantInfo


class AlipayPcreditHuabeiMerchantRecordModifyModel(object):

    def __init__(self):
        self._action = None
        self._aggr_id = None
        self._merchant_infos = None
        self._out_request_no = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def aggr_id(self):
        return self._aggr_id

    @aggr_id.setter
    def aggr_id(self, value):
        self._aggr_id = value
    @property
    def merchant_infos(self):
        return self._merchant_infos

    @merchant_infos.setter
    def merchant_infos(self, value):
        if isinstance(value, list):
            self._merchant_infos = list()
            for i in value:
                if isinstance(i, HbMerchantInfo):
                    self._merchant_infos.append(i)
                else:
                    self._merchant_infos.append(HbMerchantInfo.from_alipay_dict(i))
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.aggr_id:
            if hasattr(self.aggr_id, 'to_alipay_dict'):
                params['aggr_id'] = self.aggr_id.to_alipay_dict()
            else:
                params['aggr_id'] = self.aggr_id
        if self.merchant_infos:
            if isinstance(self.merchant_infos, list):
                for i in range(0, len(self.merchant_infos)):
                    element = self.merchant_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_infos[i] = element.to_alipay_dict()
            if hasattr(self.merchant_infos, 'to_alipay_dict'):
                params['merchant_infos'] = self.merchant_infos.to_alipay_dict()
            else:
                params['merchant_infos'] = self.merchant_infos
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiMerchantRecordModifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'aggr_id' in d:
            o.aggr_id = d['aggr_id']
        if 'merchant_infos' in d:
            o.merchant_infos = d['merchant_infos']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


