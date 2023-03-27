#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditRateResult(object):

    def __init__(self):
        self._cr_rank = None
        self._cr_rank_title = None
        self._ep_cert_no = None
        self._ep_name = None
        self._ep_status = None
        self._pass_status = None

    @property
    def cr_rank(self):
        return self._cr_rank

    @cr_rank.setter
    def cr_rank(self, value):
        self._cr_rank = value
    @property
    def cr_rank_title(self):
        return self._cr_rank_title

    @cr_rank_title.setter
    def cr_rank_title(self, value):
        self._cr_rank_title = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def ep_status(self):
        return self._ep_status

    @ep_status.setter
    def ep_status(self, value):
        self._ep_status = value
    @property
    def pass_status(self):
        return self._pass_status

    @pass_status.setter
    def pass_status(self, value):
        self._pass_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cr_rank:
            if hasattr(self.cr_rank, 'to_alipay_dict'):
                params['cr_rank'] = self.cr_rank.to_alipay_dict()
            else:
                params['cr_rank'] = self.cr_rank
        if self.cr_rank_title:
            if hasattr(self.cr_rank_title, 'to_alipay_dict'):
                params['cr_rank_title'] = self.cr_rank_title.to_alipay_dict()
            else:
                params['cr_rank_title'] = self.cr_rank_title
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.ep_status:
            if hasattr(self.ep_status, 'to_alipay_dict'):
                params['ep_status'] = self.ep_status.to_alipay_dict()
            else:
                params['ep_status'] = self.ep_status
        if self.pass_status:
            if hasattr(self.pass_status, 'to_alipay_dict'):
                params['pass_status'] = self.pass_status.to_alipay_dict()
            else:
                params['pass_status'] = self.pass_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditRateResult()
        if 'cr_rank' in d:
            o.cr_rank = d['cr_rank']
        if 'cr_rank_title' in d:
            o.cr_rank_title = d['cr_rank_title']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'ep_status' in d:
            o.ep_status = d['ep_status']
        if 'pass_status' in d:
            o.pass_status = d['pass_status']
        return o


