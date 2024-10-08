#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomeServiceInboundUpdateDTO import CustomeServiceInboundUpdateDTO
from alipay.aop.api.domain.CustomeServiceOutBoundUpdateDTO import CustomeServiceOutBoundUpdateDTO
from alipay.aop.api.domain.ServiceTicketUpdateDTO import ServiceTicketUpdateDTO


class AlipayIserviceIcontrolServiceorderModifyModel(object):

    def __init__(self):
        self._csi_payload = None
        self._cso_payload = None
        self._dispatch_mode = None
        self._order_type = None
        self._origin_service_uniq_code = None
        self._service_uniq_code = None
        self._source_id = None
        self._source_sys = None
        self._st_payload = None
        self._tnt_inst_id = None

    @property
    def csi_payload(self):
        return self._csi_payload

    @csi_payload.setter
    def csi_payload(self, value):
        if isinstance(value, CustomeServiceInboundUpdateDTO):
            self._csi_payload = value
        else:
            self._csi_payload = CustomeServiceInboundUpdateDTO.from_alipay_dict(value)
    @property
    def cso_payload(self):
        return self._cso_payload

    @cso_payload.setter
    def cso_payload(self, value):
        if isinstance(value, CustomeServiceOutBoundUpdateDTO):
            self._cso_payload = value
        else:
            self._cso_payload = CustomeServiceOutBoundUpdateDTO.from_alipay_dict(value)
    @property
    def dispatch_mode(self):
        return self._dispatch_mode

    @dispatch_mode.setter
    def dispatch_mode(self, value):
        self._dispatch_mode = value
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
    def st_payload(self):
        return self._st_payload

    @st_payload.setter
    def st_payload(self, value):
        if isinstance(value, ServiceTicketUpdateDTO):
            self._st_payload = value
        else:
            self._st_payload = ServiceTicketUpdateDTO.from_alipay_dict(value)
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.csi_payload:
            if hasattr(self.csi_payload, 'to_alipay_dict'):
                params['csi_payload'] = self.csi_payload.to_alipay_dict()
            else:
                params['csi_payload'] = self.csi_payload
        if self.cso_payload:
            if hasattr(self.cso_payload, 'to_alipay_dict'):
                params['cso_payload'] = self.cso_payload.to_alipay_dict()
            else:
                params['cso_payload'] = self.cso_payload
        if self.dispatch_mode:
            if hasattr(self.dispatch_mode, 'to_alipay_dict'):
                params['dispatch_mode'] = self.dispatch_mode.to_alipay_dict()
            else:
                params['dispatch_mode'] = self.dispatch_mode
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
        if self.st_payload:
            if hasattr(self.st_payload, 'to_alipay_dict'):
                params['st_payload'] = self.st_payload.to_alipay_dict()
            else:
                params['st_payload'] = self.st_payload
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
        o = AlipayIserviceIcontrolServiceorderModifyModel()
        if 'csi_payload' in d:
            o.csi_payload = d['csi_payload']
        if 'cso_payload' in d:
            o.cso_payload = d['cso_payload']
        if 'dispatch_mode' in d:
            o.dispatch_mode = d['dispatch_mode']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'origin_service_uniq_code' in d:
            o.origin_service_uniq_code = d['origin_service_uniq_code']
        if 'service_uniq_code' in d:
            o.service_uniq_code = d['service_uniq_code']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_sys' in d:
            o.source_sys = d['source_sys']
        if 'st_payload' in d:
            o.st_payload = d['st_payload']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


