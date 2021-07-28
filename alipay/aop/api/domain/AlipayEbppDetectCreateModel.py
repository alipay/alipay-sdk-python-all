#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DetectServiceEntity import DetectServiceEntity


class AlipayEbppDetectCreateModel(object):

    def __init__(self):
        self._biz_type = None
        self._data_from_type = None
        self._out_biz_no = None
        self._service_list = None
        self._tinyapp_id = None
        self._tinyapp_partner_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def data_from_type(self):
        return self._data_from_type

    @data_from_type.setter
    def data_from_type(self, value):
        self._data_from_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                if isinstance(i, DetectServiceEntity):
                    self._service_list.append(i)
                else:
                    self._service_list.append(DetectServiceEntity.from_alipay_dict(i))
    @property
    def tinyapp_id(self):
        return self._tinyapp_id

    @tinyapp_id.setter
    def tinyapp_id(self, value):
        self._tinyapp_id = value
    @property
    def tinyapp_partner_id(self):
        return self._tinyapp_partner_id

    @tinyapp_partner_id.setter
    def tinyapp_partner_id(self, value):
        self._tinyapp_partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.data_from_type:
            if hasattr(self.data_from_type, 'to_alipay_dict'):
                params['data_from_type'] = self.data_from_type.to_alipay_dict()
            else:
                params['data_from_type'] = self.data_from_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.service_list:
            if isinstance(self.service_list, list):
                for i in range(0, len(self.service_list)):
                    element = self.service_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_list[i] = element.to_alipay_dict()
            if hasattr(self.service_list, 'to_alipay_dict'):
                params['service_list'] = self.service_list.to_alipay_dict()
            else:
                params['service_list'] = self.service_list
        if self.tinyapp_id:
            if hasattr(self.tinyapp_id, 'to_alipay_dict'):
                params['tinyapp_id'] = self.tinyapp_id.to_alipay_dict()
            else:
                params['tinyapp_id'] = self.tinyapp_id
        if self.tinyapp_partner_id:
            if hasattr(self.tinyapp_partner_id, 'to_alipay_dict'):
                params['tinyapp_partner_id'] = self.tinyapp_partner_id.to_alipay_dict()
            else:
                params['tinyapp_partner_id'] = self.tinyapp_partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppDetectCreateModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'data_from_type' in d:
            o.data_from_type = d['data_from_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'service_list' in d:
            o.service_list = d['service_list']
        if 'tinyapp_id' in d:
            o.tinyapp_id = d['tinyapp_id']
        if 'tinyapp_partner_id' in d:
            o.tinyapp_partner_id = d['tinyapp_partner_id']
        return o


