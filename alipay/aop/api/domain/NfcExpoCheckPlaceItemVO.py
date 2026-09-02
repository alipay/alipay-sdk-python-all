#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NfcExpoCheckPlaceItemVO(object):

    def __init__(self):
        self._check_app_url = None
        self._checked = None
        self._external_place_mark = None
        self._place_full_name = None
        self._place_id = None
        self._place_name = None
        self._position = None

    @property
    def check_app_url(self):
        return self._check_app_url

    @check_app_url.setter
    def check_app_url(self, value):
        self._check_app_url = value
    @property
    def checked(self):
        return self._checked

    @checked.setter
    def checked(self, value):
        self._checked = value
    @property
    def external_place_mark(self):
        return self._external_place_mark

    @external_place_mark.setter
    def external_place_mark(self, value):
        self._external_place_mark = value
    @property
    def place_full_name(self):
        return self._place_full_name

    @place_full_name.setter
    def place_full_name(self, value):
        self._place_full_name = value
    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value
    @property
    def place_name(self):
        return self._place_name

    @place_name.setter
    def place_name(self, value):
        self._place_name = value
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_app_url:
            if hasattr(self.check_app_url, 'to_alipay_dict'):
                params['check_app_url'] = self.check_app_url.to_alipay_dict()
            else:
                params['check_app_url'] = self.check_app_url
        if self.checked:
            if hasattr(self.checked, 'to_alipay_dict'):
                params['checked'] = self.checked.to_alipay_dict()
            else:
                params['checked'] = self.checked
        if self.external_place_mark:
            if hasattr(self.external_place_mark, 'to_alipay_dict'):
                params['external_place_mark'] = self.external_place_mark.to_alipay_dict()
            else:
                params['external_place_mark'] = self.external_place_mark
        if self.place_full_name:
            if hasattr(self.place_full_name, 'to_alipay_dict'):
                params['place_full_name'] = self.place_full_name.to_alipay_dict()
            else:
                params['place_full_name'] = self.place_full_name
        if self.place_id:
            if hasattr(self.place_id, 'to_alipay_dict'):
                params['place_id'] = self.place_id.to_alipay_dict()
            else:
                params['place_id'] = self.place_id
        if self.place_name:
            if hasattr(self.place_name, 'to_alipay_dict'):
                params['place_name'] = self.place_name.to_alipay_dict()
            else:
                params['place_name'] = self.place_name
        if self.position:
            if hasattr(self.position, 'to_alipay_dict'):
                params['position'] = self.position.to_alipay_dict()
            else:
                params['position'] = self.position
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NfcExpoCheckPlaceItemVO()
        if 'check_app_url' in d:
            o.check_app_url = d['check_app_url']
        if 'checked' in d:
            o.checked = d['checked']
        if 'external_place_mark' in d:
            o.external_place_mark = d['external_place_mark']
        if 'place_full_name' in d:
            o.place_full_name = d['place_full_name']
        if 'place_id' in d:
            o.place_id = d['place_id']
        if 'place_name' in d:
            o.place_name = d['place_name']
        if 'position' in d:
            o.position = d['position']
        return o


