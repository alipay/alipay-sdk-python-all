#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoAutoinsprodUserCertifyModel(object):

    def __init__(self):
        self._agent_id_card_name = None
        self._agent_id_card_no = None
        self._agent_user_id = None
        self._auth_cert_name = None
        self._auth_cert_no = None

    @property
    def agent_id_card_name(self):
        return self._agent_id_card_name

    @agent_id_card_name.setter
    def agent_id_card_name(self, value):
        self._agent_id_card_name = value
    @property
    def agent_id_card_no(self):
        return self._agent_id_card_no

    @agent_id_card_no.setter
    def agent_id_card_no(self, value):
        self._agent_id_card_no = value
    @property
    def agent_user_id(self):
        return self._agent_user_id

    @agent_user_id.setter
    def agent_user_id(self, value):
        self._agent_user_id = value
    @property
    def auth_cert_name(self):
        return self._auth_cert_name

    @auth_cert_name.setter
    def auth_cert_name(self, value):
        self._auth_cert_name = value
    @property
    def auth_cert_no(self):
        return self._auth_cert_no

    @auth_cert_no.setter
    def auth_cert_no(self, value):
        self._auth_cert_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id_card_name:
            if hasattr(self.agent_id_card_name, 'to_alipay_dict'):
                params['agent_id_card_name'] = self.agent_id_card_name.to_alipay_dict()
            else:
                params['agent_id_card_name'] = self.agent_id_card_name
        if self.agent_id_card_no:
            if hasattr(self.agent_id_card_no, 'to_alipay_dict'):
                params['agent_id_card_no'] = self.agent_id_card_no.to_alipay_dict()
            else:
                params['agent_id_card_no'] = self.agent_id_card_no
        if self.agent_user_id:
            if hasattr(self.agent_user_id, 'to_alipay_dict'):
                params['agent_user_id'] = self.agent_user_id.to_alipay_dict()
            else:
                params['agent_user_id'] = self.agent_user_id
        if self.auth_cert_name:
            if hasattr(self.auth_cert_name, 'to_alipay_dict'):
                params['auth_cert_name'] = self.auth_cert_name.to_alipay_dict()
            else:
                params['auth_cert_name'] = self.auth_cert_name
        if self.auth_cert_no:
            if hasattr(self.auth_cert_no, 'to_alipay_dict'):
                params['auth_cert_no'] = self.auth_cert_no.to_alipay_dict()
            else:
                params['auth_cert_no'] = self.auth_cert_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoAutoinsprodUserCertifyModel()
        if 'agent_id_card_name' in d:
            o.agent_id_card_name = d['agent_id_card_name']
        if 'agent_id_card_no' in d:
            o.agent_id_card_no = d['agent_id_card_no']
        if 'agent_user_id' in d:
            o.agent_user_id = d['agent_user_id']
        if 'auth_cert_name' in d:
            o.auth_cert_name = d['auth_cert_name']
        if 'auth_cert_no' in d:
            o.auth_cert_no = d['auth_cert_no']
        return o


