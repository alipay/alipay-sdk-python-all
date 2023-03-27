#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcProtocolInfo import EcProtocolInfo


class EcContractInfo(object):

    def __init__(self):
        self._cancel_time = None
        self._contract_id = None
        self._contract_title = None
        self._first_party_id = None
        self._first_party_name = None
        self._out_request_no = None
        self._protocol_info_list = None
        self._scene = None
        self._second_party_id = None
        self._second_party_name = None
        self._sign_time = None
        self._status = None

    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def contract_title(self):
        return self._contract_title

    @contract_title.setter
    def contract_title(self, value):
        self._contract_title = value
    @property
    def first_party_id(self):
        return self._first_party_id

    @first_party_id.setter
    def first_party_id(self, value):
        self._first_party_id = value
    @property
    def first_party_name(self):
        return self._first_party_name

    @first_party_name.setter
    def first_party_name(self, value):
        self._first_party_name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def protocol_info_list(self):
        return self._protocol_info_list

    @protocol_info_list.setter
    def protocol_info_list(self, value):
        if isinstance(value, list):
            self._protocol_info_list = list()
            for i in value:
                if isinstance(i, EcProtocolInfo):
                    self._protocol_info_list.append(i)
                else:
                    self._protocol_info_list.append(EcProtocolInfo.from_alipay_dict(i))
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def second_party_id(self):
        return self._second_party_id

    @second_party_id.setter
    def second_party_id(self, value):
        self._second_party_id = value
    @property
    def second_party_name(self):
        return self._second_party_name

    @second_party_name.setter
    def second_party_name(self, value):
        self._second_party_name = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.contract_title:
            if hasattr(self.contract_title, 'to_alipay_dict'):
                params['contract_title'] = self.contract_title.to_alipay_dict()
            else:
                params['contract_title'] = self.contract_title
        if self.first_party_id:
            if hasattr(self.first_party_id, 'to_alipay_dict'):
                params['first_party_id'] = self.first_party_id.to_alipay_dict()
            else:
                params['first_party_id'] = self.first_party_id
        if self.first_party_name:
            if hasattr(self.first_party_name, 'to_alipay_dict'):
                params['first_party_name'] = self.first_party_name.to_alipay_dict()
            else:
                params['first_party_name'] = self.first_party_name
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.protocol_info_list:
            if isinstance(self.protocol_info_list, list):
                for i in range(0, len(self.protocol_info_list)):
                    element = self.protocol_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.protocol_info_list[i] = element.to_alipay_dict()
            if hasattr(self.protocol_info_list, 'to_alipay_dict'):
                params['protocol_info_list'] = self.protocol_info_list.to_alipay_dict()
            else:
                params['protocol_info_list'] = self.protocol_info_list
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.second_party_id:
            if hasattr(self.second_party_id, 'to_alipay_dict'):
                params['second_party_id'] = self.second_party_id.to_alipay_dict()
            else:
                params['second_party_id'] = self.second_party_id
        if self.second_party_name:
            if hasattr(self.second_party_name, 'to_alipay_dict'):
                params['second_party_name'] = self.second_party_name.to_alipay_dict()
            else:
                params['second_party_name'] = self.second_party_name
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcContractInfo()
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'contract_title' in d:
            o.contract_title = d['contract_title']
        if 'first_party_id' in d:
            o.first_party_id = d['first_party_id']
        if 'first_party_name' in d:
            o.first_party_name = d['first_party_name']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'protocol_info_list' in d:
            o.protocol_info_list = d['protocol_info_list']
        if 'scene' in d:
            o.scene = d['scene']
        if 'second_party_id' in d:
            o.second_party_id = d['second_party_id']
        if 'second_party_name' in d:
            o.second_party_name = d['second_party_name']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'status' in d:
            o.status = d['status']
        return o


