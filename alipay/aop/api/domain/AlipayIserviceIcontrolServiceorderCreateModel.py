#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomeServiceInboundCreateDTO import CustomeServiceInboundCreateDTO
from alipay.aop.api.domain.CustomeServiceOutboundCreateDTO import CustomeServiceOutboundCreateDTO
from alipay.aop.api.domain.FirstSloved import FirstSloved
from alipay.aop.api.domain.Satisfaction import Satisfaction
from alipay.aop.api.domain.ServiceTicketCreateDTO import ServiceTicketCreateDTO


class AlipayIserviceIcontrolServiceorderCreateModel(object):

    def __init__(self):
        self._csi_order_data = None
        self._cso_order_data = None
        self._dispatch_mode = None
        self._first_sloved = None
        self._order_time = None
        self._order_type = None
        self._origin_service_uniq_code = None
        self._satisfaction = None
        self._service_uniq_code = None
        self._source_id = None
        self._source_sys = None
        self._st_order_data = None
        self._tnt_inst_id = None

    @property
    def csi_order_data(self):
        return self._csi_order_data

    @csi_order_data.setter
    def csi_order_data(self, value):
        if isinstance(value, CustomeServiceInboundCreateDTO):
            self._csi_order_data = value
        else:
            self._csi_order_data = CustomeServiceInboundCreateDTO.from_alipay_dict(value)
    @property
    def cso_order_data(self):
        return self._cso_order_data

    @cso_order_data.setter
    def cso_order_data(self, value):
        if isinstance(value, CustomeServiceOutboundCreateDTO):
            self._cso_order_data = value
        else:
            self._cso_order_data = CustomeServiceOutboundCreateDTO.from_alipay_dict(value)
    @property
    def dispatch_mode(self):
        return self._dispatch_mode

    @dispatch_mode.setter
    def dispatch_mode(self, value):
        self._dispatch_mode = value
    @property
    def first_sloved(self):
        return self._first_sloved

    @first_sloved.setter
    def first_sloved(self, value):
        if isinstance(value, FirstSloved):
            self._first_sloved = value
        else:
            self._first_sloved = FirstSloved.from_alipay_dict(value)
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def origin_service_uniq_code(self):
        return self._origin_service_uniq_code

    @origin_service_uniq_code.setter
    def origin_service_uniq_code(self, value):
        self._origin_service_uniq_code = value
    @property
    def satisfaction(self):
        return self._satisfaction

    @satisfaction.setter
    def satisfaction(self, value):
        if isinstance(value, Satisfaction):
            self._satisfaction = value
        else:
            self._satisfaction = Satisfaction.from_alipay_dict(value)
    @property
    def service_uniq_code(self):
        return self._service_uniq_code

    @service_uniq_code.setter
    def service_uniq_code(self, value):
        self._service_uniq_code = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_sys(self):
        return self._source_sys

    @source_sys.setter
    def source_sys(self, value):
        self._source_sys = value
    @property
    def st_order_data(self):
        return self._st_order_data

    @st_order_data.setter
    def st_order_data(self, value):
        if isinstance(value, ServiceTicketCreateDTO):
            self._st_order_data = value
        else:
            self._st_order_data = ServiceTicketCreateDTO.from_alipay_dict(value)
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.csi_order_data:
            if hasattr(self.csi_order_data, 'to_alipay_dict'):
                params['csi_order_data'] = self.csi_order_data.to_alipay_dict()
            else:
                params['csi_order_data'] = self.csi_order_data
        if self.cso_order_data:
            if hasattr(self.cso_order_data, 'to_alipay_dict'):
                params['cso_order_data'] = self.cso_order_data.to_alipay_dict()
            else:
                params['cso_order_data'] = self.cso_order_data
        if self.dispatch_mode:
            if hasattr(self.dispatch_mode, 'to_alipay_dict'):
                params['dispatch_mode'] = self.dispatch_mode.to_alipay_dict()
            else:
                params['dispatch_mode'] = self.dispatch_mode
        if self.first_sloved:
            if hasattr(self.first_sloved, 'to_alipay_dict'):
                params['first_sloved'] = self.first_sloved.to_alipay_dict()
            else:
                params['first_sloved'] = self.first_sloved
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.origin_service_uniq_code:
            if hasattr(self.origin_service_uniq_code, 'to_alipay_dict'):
                params['origin_service_uniq_code'] = self.origin_service_uniq_code.to_alipay_dict()
            else:
                params['origin_service_uniq_code'] = self.origin_service_uniq_code
        if self.satisfaction:
            if hasattr(self.satisfaction, 'to_alipay_dict'):
                params['satisfaction'] = self.satisfaction.to_alipay_dict()
            else:
                params['satisfaction'] = self.satisfaction
        if self.service_uniq_code:
            if hasattr(self.service_uniq_code, 'to_alipay_dict'):
                params['service_uniq_code'] = self.service_uniq_code.to_alipay_dict()
            else:
                params['service_uniq_code'] = self.service_uniq_code
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.source_sys:
            if hasattr(self.source_sys, 'to_alipay_dict'):
                params['source_sys'] = self.source_sys.to_alipay_dict()
            else:
                params['source_sys'] = self.source_sys
        if self.st_order_data:
            if hasattr(self.st_order_data, 'to_alipay_dict'):
                params['st_order_data'] = self.st_order_data.to_alipay_dict()
            else:
                params['st_order_data'] = self.st_order_data
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
        o = AlipayIserviceIcontrolServiceorderCreateModel()
        if 'csi_order_data' in d:
            o.csi_order_data = d['csi_order_data']
        if 'cso_order_data' in d:
            o.cso_order_data = d['cso_order_data']
        if 'dispatch_mode' in d:
            o.dispatch_mode = d['dispatch_mode']
        if 'first_sloved' in d:
            o.first_sloved = d['first_sloved']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'origin_service_uniq_code' in d:
            o.origin_service_uniq_code = d['origin_service_uniq_code']
        if 'satisfaction' in d:
            o.satisfaction = d['satisfaction']
        if 'service_uniq_code' in d:
            o.service_uniq_code = d['service_uniq_code']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_sys' in d:
            o.source_sys = d['source_sys']
        if 'st_order_data' in d:
            o.st_order_data = d['st_order_data']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


