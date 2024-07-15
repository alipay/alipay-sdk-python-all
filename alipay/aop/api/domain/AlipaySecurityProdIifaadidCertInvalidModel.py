#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IifaaDidCdidDetail import IifaaDidCdidDetail


class AlipaySecurityProdIifaadidCertInvalidModel(object):

    def __init__(self):
        self._batch_number = None
        self._bsn = None
        self._cdid_list = None
        self._similar_notice = None
        self._time_stamp = None

    @property
    def batch_number(self):
        return self._batch_number

    @batch_number.setter
    def batch_number(self, value):
        self._batch_number = value
    @property
    def bsn(self):
        return self._bsn

    @bsn.setter
    def bsn(self, value):
        self._bsn = value
    @property
    def cdid_list(self):
        return self._cdid_list

    @cdid_list.setter
    def cdid_list(self, value):
        if isinstance(value, list):
            self._cdid_list = list()
            for i in value:
                if isinstance(i, IifaaDidCdidDetail):
                    self._cdid_list.append(i)
                else:
                    self._cdid_list.append(IifaaDidCdidDetail.from_alipay_dict(i))
    @property
    def similar_notice(self):
        return self._similar_notice

    @similar_notice.setter
    def similar_notice(self, value):
        self._similar_notice = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_number:
            if hasattr(self.batch_number, 'to_alipay_dict'):
                params['batch_number'] = self.batch_number.to_alipay_dict()
            else:
                params['batch_number'] = self.batch_number
        if self.bsn:
            if hasattr(self.bsn, 'to_alipay_dict'):
                params['bsn'] = self.bsn.to_alipay_dict()
            else:
                params['bsn'] = self.bsn
        if self.cdid_list:
            if isinstance(self.cdid_list, list):
                for i in range(0, len(self.cdid_list)):
                    element = self.cdid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cdid_list[i] = element.to_alipay_dict()
            if hasattr(self.cdid_list, 'to_alipay_dict'):
                params['cdid_list'] = self.cdid_list.to_alipay_dict()
            else:
                params['cdid_list'] = self.cdid_list
        if self.similar_notice:
            if hasattr(self.similar_notice, 'to_alipay_dict'):
                params['similar_notice'] = self.similar_notice.to_alipay_dict()
            else:
                params['similar_notice'] = self.similar_notice
        if self.time_stamp:
            if hasattr(self.time_stamp, 'to_alipay_dict'):
                params['time_stamp'] = self.time_stamp.to_alipay_dict()
            else:
                params['time_stamp'] = self.time_stamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdIifaadidCertInvalidModel()
        if 'batch_number' in d:
            o.batch_number = d['batch_number']
        if 'bsn' in d:
            o.bsn = d['bsn']
        if 'cdid_list' in d:
            o.cdid_list = d['cdid_list']
        if 'similar_notice' in d:
            o.similar_notice = d['similar_notice']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        return o


