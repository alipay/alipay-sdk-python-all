#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GFAOpenAPIAccountingAcceptance(object):

    def __init__(self):
        self._amount_map = None
        self._biz_bill_nos_map = None
        self._biz_elements = None
        self._biz_ev_code = None
        self._biz_pd_code = None
        self._cnl_ev_code = None
        self._cnl_pd_code = None
        self._gmt_service = None
        self._high_amount_map = None
        self._inst_code = None
        self._memo = None
        self._out_business_no = None
        self._properties = None
        self._service_type = None
        self._sub_out_business_no = None
        self._system_origin = None
        self._tnt_inst_id = None

    @property
    def amount_map(self):
        return self._amount_map

    @amount_map.setter
    def amount_map(self, value):
        self._amount_map = value
    @property
    def biz_bill_nos_map(self):
        return self._biz_bill_nos_map

    @biz_bill_nos_map.setter
    def biz_bill_nos_map(self, value):
        self._biz_bill_nos_map = value
    @property
    def biz_elements(self):
        return self._biz_elements

    @biz_elements.setter
    def biz_elements(self, value):
        self._biz_elements = value
    @property
    def biz_ev_code(self):
        return self._biz_ev_code

    @biz_ev_code.setter
    def biz_ev_code(self, value):
        self._biz_ev_code = value
    @property
    def biz_pd_code(self):
        return self._biz_pd_code

    @biz_pd_code.setter
    def biz_pd_code(self, value):
        self._biz_pd_code = value
    @property
    def cnl_ev_code(self):
        return self._cnl_ev_code

    @cnl_ev_code.setter
    def cnl_ev_code(self, value):
        self._cnl_ev_code = value
    @property
    def cnl_pd_code(self):
        return self._cnl_pd_code

    @cnl_pd_code.setter
    def cnl_pd_code(self, value):
        self._cnl_pd_code = value
    @property
    def gmt_service(self):
        return self._gmt_service

    @gmt_service.setter
    def gmt_service(self, value):
        self._gmt_service = value
    @property
    def high_amount_map(self):
        return self._high_amount_map

    @high_amount_map.setter
    def high_amount_map(self, value):
        self._high_amount_map = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_business_no(self):
        return self._out_business_no

    @out_business_no.setter
    def out_business_no(self, value):
        self._out_business_no = value
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        self._properties = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def sub_out_business_no(self):
        return self._sub_out_business_no

    @sub_out_business_no.setter
    def sub_out_business_no(self, value):
        self._sub_out_business_no = value
    @property
    def system_origin(self):
        return self._system_origin

    @system_origin.setter
    def system_origin(self, value):
        self._system_origin = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_map:
            if hasattr(self.amount_map, 'to_alipay_dict'):
                params['amount_map'] = self.amount_map.to_alipay_dict()
            else:
                params['amount_map'] = self.amount_map
        if self.biz_bill_nos_map:
            if hasattr(self.biz_bill_nos_map, 'to_alipay_dict'):
                params['biz_bill_nos_map'] = self.biz_bill_nos_map.to_alipay_dict()
            else:
                params['biz_bill_nos_map'] = self.biz_bill_nos_map
        if self.biz_elements:
            if hasattr(self.biz_elements, 'to_alipay_dict'):
                params['biz_elements'] = self.biz_elements.to_alipay_dict()
            else:
                params['biz_elements'] = self.biz_elements
        if self.biz_ev_code:
            if hasattr(self.biz_ev_code, 'to_alipay_dict'):
                params['biz_ev_code'] = self.biz_ev_code.to_alipay_dict()
            else:
                params['biz_ev_code'] = self.biz_ev_code
        if self.biz_pd_code:
            if hasattr(self.biz_pd_code, 'to_alipay_dict'):
                params['biz_pd_code'] = self.biz_pd_code.to_alipay_dict()
            else:
                params['biz_pd_code'] = self.biz_pd_code
        if self.cnl_ev_code:
            if hasattr(self.cnl_ev_code, 'to_alipay_dict'):
                params['cnl_ev_code'] = self.cnl_ev_code.to_alipay_dict()
            else:
                params['cnl_ev_code'] = self.cnl_ev_code
        if self.cnl_pd_code:
            if hasattr(self.cnl_pd_code, 'to_alipay_dict'):
                params['cnl_pd_code'] = self.cnl_pd_code.to_alipay_dict()
            else:
                params['cnl_pd_code'] = self.cnl_pd_code
        if self.gmt_service:
            if hasattr(self.gmt_service, 'to_alipay_dict'):
                params['gmt_service'] = self.gmt_service.to_alipay_dict()
            else:
                params['gmt_service'] = self.gmt_service
        if self.high_amount_map:
            if hasattr(self.high_amount_map, 'to_alipay_dict'):
                params['high_amount_map'] = self.high_amount_map.to_alipay_dict()
            else:
                params['high_amount_map'] = self.high_amount_map
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_business_no:
            if hasattr(self.out_business_no, 'to_alipay_dict'):
                params['out_business_no'] = self.out_business_no.to_alipay_dict()
            else:
                params['out_business_no'] = self.out_business_no
        if self.properties:
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.sub_out_business_no:
            if hasattr(self.sub_out_business_no, 'to_alipay_dict'):
                params['sub_out_business_no'] = self.sub_out_business_no.to_alipay_dict()
            else:
                params['sub_out_business_no'] = self.sub_out_business_no
        if self.system_origin:
            if hasattr(self.system_origin, 'to_alipay_dict'):
                params['system_origin'] = self.system_origin.to_alipay_dict()
            else:
                params['system_origin'] = self.system_origin
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIAccountingAcceptance()
        if 'amount_map' in d:
            o.amount_map = d['amount_map']
        if 'biz_bill_nos_map' in d:
            o.biz_bill_nos_map = d['biz_bill_nos_map']
        if 'biz_elements' in d:
            o.biz_elements = d['biz_elements']
        if 'biz_ev_code' in d:
            o.biz_ev_code = d['biz_ev_code']
        if 'biz_pd_code' in d:
            o.biz_pd_code = d['biz_pd_code']
        if 'cnl_ev_code' in d:
            o.cnl_ev_code = d['cnl_ev_code']
        if 'cnl_pd_code' in d:
            o.cnl_pd_code = d['cnl_pd_code']
        if 'gmt_service' in d:
            o.gmt_service = d['gmt_service']
        if 'high_amount_map' in d:
            o.high_amount_map = d['high_amount_map']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_business_no' in d:
            o.out_business_no = d['out_business_no']
        if 'properties' in d:
            o.properties = d['properties']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'sub_out_business_no' in d:
            o.sub_out_business_no = d['sub_out_business_no']
        if 'system_origin' in d:
            o.system_origin = d['system_origin']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


