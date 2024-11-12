#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenePayParticipantBizParamDTO(object):

    def __init__(self):
        self._authorization_id = None
        self._cert_no = None
        self._cert_type = None
        self._channel_id = None
        self._city_traffic_industry_tag = None
        self._out_card_no = None
        self._user_name = None

    @property
    def authorization_id(self):
        return self._authorization_id

    @authorization_id.setter
    def authorization_id(self, value):
        self._authorization_id = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def city_traffic_industry_tag(self):
        return self._city_traffic_industry_tag

    @city_traffic_industry_tag.setter
    def city_traffic_industry_tag(self, value):
        self._city_traffic_industry_tag = value
    @property
    def out_card_no(self):
        return self._out_card_no

    @out_card_no.setter
    def out_card_no(self, value):
        self._out_card_no = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorization_id:
            if hasattr(self.authorization_id, 'to_alipay_dict'):
                params['authorization_id'] = self.authorization_id.to_alipay_dict()
            else:
                params['authorization_id'] = self.authorization_id
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.city_traffic_industry_tag:
            if hasattr(self.city_traffic_industry_tag, 'to_alipay_dict'):
                params['city_traffic_industry_tag'] = self.city_traffic_industry_tag.to_alipay_dict()
            else:
                params['city_traffic_industry_tag'] = self.city_traffic_industry_tag
        if self.out_card_no:
            if hasattr(self.out_card_no, 'to_alipay_dict'):
                params['out_card_no'] = self.out_card_no.to_alipay_dict()
            else:
                params['out_card_no'] = self.out_card_no
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenePayParticipantBizParamDTO()
        if 'authorization_id' in d:
            o.authorization_id = d['authorization_id']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'city_traffic_industry_tag' in d:
            o.city_traffic_industry_tag = d['city_traffic_industry_tag']
        if 'out_card_no' in d:
            o.out_card_no = d['out_card_no']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


