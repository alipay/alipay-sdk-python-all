#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EtcVehicleInfo import EtcVehicleInfo
from alipay.aop.api.domain.EtcVehicleOwnerInfo import EtcVehicleOwnerInfo


class AlipayCommerceTransportEtcenterpriseVehicleCreateModel(object):

    def __init__(self):
        self._agent_cert_no = None
        self._agent_cert_type = None
        self._agent_name = None
        self._corp_id = None
        self._corp_vehicle_id = None
        self._vehicle_corp_id = None
        self._vehicle_info = None
        self._vehicle_owner_info = None

    @property
    def agent_cert_no(self):
        return self._agent_cert_no

    @agent_cert_no.setter
    def agent_cert_no(self, value):
        self._agent_cert_no = value
    @property
    def agent_cert_type(self):
        return self._agent_cert_type

    @agent_cert_type.setter
    def agent_cert_type(self, value):
        self._agent_cert_type = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def corp_vehicle_id(self):
        return self._corp_vehicle_id

    @corp_vehicle_id.setter
    def corp_vehicle_id(self, value):
        self._corp_vehicle_id = value
    @property
    def vehicle_corp_id(self):
        return self._vehicle_corp_id

    @vehicle_corp_id.setter
    def vehicle_corp_id(self, value):
        self._vehicle_corp_id = value
    @property
    def vehicle_info(self):
        return self._vehicle_info

    @vehicle_info.setter
    def vehicle_info(self, value):
        if isinstance(value, EtcVehicleInfo):
            self._vehicle_info = value
        else:
            self._vehicle_info = EtcVehicleInfo.from_alipay_dict(value)
    @property
    def vehicle_owner_info(self):
        return self._vehicle_owner_info

    @vehicle_owner_info.setter
    def vehicle_owner_info(self, value):
        if isinstance(value, EtcVehicleOwnerInfo):
            self._vehicle_owner_info = value
        else:
            self._vehicle_owner_info = EtcVehicleOwnerInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.agent_cert_no:
            if hasattr(self.agent_cert_no, 'to_alipay_dict'):
                params['agent_cert_no'] = self.agent_cert_no.to_alipay_dict()
            else:
                params['agent_cert_no'] = self.agent_cert_no
        if self.agent_cert_type:
            if hasattr(self.agent_cert_type, 'to_alipay_dict'):
                params['agent_cert_type'] = self.agent_cert_type.to_alipay_dict()
            else:
                params['agent_cert_type'] = self.agent_cert_type
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.corp_vehicle_id:
            if hasattr(self.corp_vehicle_id, 'to_alipay_dict'):
                params['corp_vehicle_id'] = self.corp_vehicle_id.to_alipay_dict()
            else:
                params['corp_vehicle_id'] = self.corp_vehicle_id
        if self.vehicle_corp_id:
            if hasattr(self.vehicle_corp_id, 'to_alipay_dict'):
                params['vehicle_corp_id'] = self.vehicle_corp_id.to_alipay_dict()
            else:
                params['vehicle_corp_id'] = self.vehicle_corp_id
        if self.vehicle_info:
            if hasattr(self.vehicle_info, 'to_alipay_dict'):
                params['vehicle_info'] = self.vehicle_info.to_alipay_dict()
            else:
                params['vehicle_info'] = self.vehicle_info
        if self.vehicle_owner_info:
            if hasattr(self.vehicle_owner_info, 'to_alipay_dict'):
                params['vehicle_owner_info'] = self.vehicle_owner_info.to_alipay_dict()
            else:
                params['vehicle_owner_info'] = self.vehicle_owner_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcenterpriseVehicleCreateModel()
        if 'agent_cert_no' in d:
            o.agent_cert_no = d['agent_cert_no']
        if 'agent_cert_type' in d:
            o.agent_cert_type = d['agent_cert_type']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'corp_vehicle_id' in d:
            o.corp_vehicle_id = d['corp_vehicle_id']
        if 'vehicle_corp_id' in d:
            o.vehicle_corp_id = d['vehicle_corp_id']
        if 'vehicle_info' in d:
            o.vehicle_info = d['vehicle_info']
        if 'vehicle_owner_info' in d:
            o.vehicle_owner_info = d['vehicle_owner_info']
        return o


