#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YpzMedAccompanyCardOne(object):

    def __init__(self):
        self._attendant_name = None
        self._redirect_url = None
        self._redirect_url_left = None
        self._redirect_url_right = None
        self._status = None

    @property
    def attendant_name(self):
        return self._attendant_name

    @attendant_name.setter
    def attendant_name(self, value):
        self._attendant_name = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def redirect_url_left(self):
        return self._redirect_url_left

    @redirect_url_left.setter
    def redirect_url_left(self, value):
        self._redirect_url_left = value
    @property
    def redirect_url_right(self):
        return self._redirect_url_right

    @redirect_url_right.setter
    def redirect_url_right(self, value):
        self._redirect_url_right = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.attendant_name:
            if hasattr(self.attendant_name, 'to_alipay_dict'):
                params['attendant_name'] = self.attendant_name.to_alipay_dict()
            else:
                params['attendant_name'] = self.attendant_name
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.redirect_url_left:
            if hasattr(self.redirect_url_left, 'to_alipay_dict'):
                params['redirect_url_left'] = self.redirect_url_left.to_alipay_dict()
            else:
                params['redirect_url_left'] = self.redirect_url_left
        if self.redirect_url_right:
            if hasattr(self.redirect_url_right, 'to_alipay_dict'):
                params['redirect_url_right'] = self.redirect_url_right.to_alipay_dict()
            else:
                params['redirect_url_right'] = self.redirect_url_right
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
        o = YpzMedAccompanyCardOne()
        if 'attendant_name' in d:
            o.attendant_name = d['attendant_name']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'redirect_url_left' in d:
            o.redirect_url_left = d['redirect_url_left']
        if 'redirect_url_right' in d:
            o.redirect_url_right = d['redirect_url_right']
        if 'status' in d:
            o.status = d['status']
        return o


