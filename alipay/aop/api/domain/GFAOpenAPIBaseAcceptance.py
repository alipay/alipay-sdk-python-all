#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GFAOpenAPIBaseAcceptance(object):

    def __init__(self):
        self._acceptance_id = None
        self._biz_ev_code = None
        self._biz_pd_code = None
        self._cnl_ev_code = None
        self._cnl_pd_code = None
        self._direction = None
        self._identity_id = None
        self._out_business_no = None
        self._principal_id = None
        self._properties = None
        self._rel_out_business_no = None
        self._rel_sub_out_business_no = None
        self._service_type = None
        self._solution_id = None
        self._sub_out_business_no = None
        self._system_origin = None

    @property
    def acceptance_id(self):
        return self._acceptance_id

    @acceptance_id.setter
    def acceptance_id(self, value):
        self._acceptance_id = value
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
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def out_business_no(self):
        return self._out_business_no

    @out_business_no.setter
    def out_business_no(self, value):
        self._out_business_no = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        self._properties = value
    @property
    def rel_out_business_no(self):
        return self._rel_out_business_no

    @rel_out_business_no.setter
    def rel_out_business_no(self, value):
        self._rel_out_business_no = value
    @property
    def rel_sub_out_business_no(self):
        return self._rel_sub_out_business_no

    @rel_sub_out_business_no.setter
    def rel_sub_out_business_no(self, value):
        self._rel_sub_out_business_no = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.acceptance_id:
            if hasattr(self.acceptance_id, 'to_alipay_dict'):
                params['acceptance_id'] = self.acceptance_id.to_alipay_dict()
            else:
                params['acceptance_id'] = self.acceptance_id
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
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        if self.out_business_no:
            if hasattr(self.out_business_no, 'to_alipay_dict'):
                params['out_business_no'] = self.out_business_no.to_alipay_dict()
            else:
                params['out_business_no'] = self.out_business_no
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.properties:
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        if self.rel_out_business_no:
            if hasattr(self.rel_out_business_no, 'to_alipay_dict'):
                params['rel_out_business_no'] = self.rel_out_business_no.to_alipay_dict()
            else:
                params['rel_out_business_no'] = self.rel_out_business_no
        if self.rel_sub_out_business_no:
            if hasattr(self.rel_sub_out_business_no, 'to_alipay_dict'):
                params['rel_sub_out_business_no'] = self.rel_sub_out_business_no.to_alipay_dict()
            else:
                params['rel_sub_out_business_no'] = self.rel_sub_out_business_no
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIBaseAcceptance()
        if 'acceptance_id' in d:
            o.acceptance_id = d['acceptance_id']
        if 'biz_ev_code' in d:
            o.biz_ev_code = d['biz_ev_code']
        if 'biz_pd_code' in d:
            o.biz_pd_code = d['biz_pd_code']
        if 'cnl_ev_code' in d:
            o.cnl_ev_code = d['cnl_ev_code']
        if 'cnl_pd_code' in d:
            o.cnl_pd_code = d['cnl_pd_code']
        if 'direction' in d:
            o.direction = d['direction']
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'out_business_no' in d:
            o.out_business_no = d['out_business_no']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'properties' in d:
            o.properties = d['properties']
        if 'rel_out_business_no' in d:
            o.rel_out_business_no = d['rel_out_business_no']
        if 'rel_sub_out_business_no' in d:
            o.rel_sub_out_business_no = d['rel_sub_out_business_no']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        if 'sub_out_business_no' in d:
            o.sub_out_business_no = d['sub_out_business_no']
        if 'system_origin' in d:
            o.system_origin = d['system_origin']
        return o


