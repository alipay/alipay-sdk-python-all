#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserAuthAgreement(object):

    def __init__(self):
        self._agreement_name = None
        self._download_link = None
        self._link = None

    @property
    def agreement_name(self):
        return self._agreement_name

    @agreement_name.setter
    def agreement_name(self, value):
        self._agreement_name = value
    @property
    def download_link(self):
        return self._download_link

    @download_link.setter
    def download_link(self, value):
        self._download_link = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_name:
            if hasattr(self.agreement_name, 'to_alipay_dict'):
                params['agreement_name'] = self.agreement_name.to_alipay_dict()
            else:
                params['agreement_name'] = self.agreement_name
        if self.download_link:
            if hasattr(self.download_link, 'to_alipay_dict'):
                params['download_link'] = self.download_link.to_alipay_dict()
            else:
                params['download_link'] = self.download_link
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserAuthAgreement()
        if 'agreement_name' in d:
            o.agreement_name = d['agreement_name']
        if 'download_link' in d:
            o.download_link = d['download_link']
        if 'link' in d:
            o.link = d['link']
        return o


