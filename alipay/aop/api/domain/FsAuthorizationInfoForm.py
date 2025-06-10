#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FsAuthorizationInfoForm(object):

    def __init__(self):
        self._authorized_domains = None
        self._authorized_users = None

    @property
    def authorized_domains(self):
        return self._authorized_domains

    @authorized_domains.setter
    def authorized_domains(self, value):
        if isinstance(value, list):
            self._authorized_domains = list()
            for i in value:
                self._authorized_domains.append(i)
    @property
    def authorized_users(self):
        return self._authorized_users

    @authorized_users.setter
    def authorized_users(self, value):
        if isinstance(value, list):
            self._authorized_users = list()
            for i in value:
                self._authorized_users.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.authorized_domains:
            if isinstance(self.authorized_domains, list):
                for i in range(0, len(self.authorized_domains)):
                    element = self.authorized_domains[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authorized_domains[i] = element.to_alipay_dict()
            if hasattr(self.authorized_domains, 'to_alipay_dict'):
                params['authorized_domains'] = self.authorized_domains.to_alipay_dict()
            else:
                params['authorized_domains'] = self.authorized_domains
        if self.authorized_users:
            if isinstance(self.authorized_users, list):
                for i in range(0, len(self.authorized_users)):
                    element = self.authorized_users[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authorized_users[i] = element.to_alipay_dict()
            if hasattr(self.authorized_users, 'to_alipay_dict'):
                params['authorized_users'] = self.authorized_users.to_alipay_dict()
            else:
                params['authorized_users'] = self.authorized_users
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FsAuthorizationInfoForm()
        if 'authorized_domains' in d:
            o.authorized_domains = d['authorized_domains']
        if 'authorized_users' in d:
            o.authorized_users = d['authorized_users']
        return o


