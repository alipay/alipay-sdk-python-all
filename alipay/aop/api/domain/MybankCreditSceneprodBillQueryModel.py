#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodBillQueryModel(object):

    def __init__(self):
        self._app_seqno = None
        self._drawdown_no = None
        self._ext_param = None
        self._site = None
        self._site_user_id = None

    @property
    def app_seqno(self):
        return self._app_seqno

    @app_seqno.setter
    def app_seqno(self, value):
        self._app_seqno = value
    @property
    def drawdown_no(self):
        return self._drawdown_no

    @drawdown_no.setter
    def drawdown_no(self, value):
        self._drawdown_no = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_seqno:
            if hasattr(self.app_seqno, 'to_alipay_dict'):
                params['app_seqno'] = self.app_seqno.to_alipay_dict()
            else:
                params['app_seqno'] = self.app_seqno
        if self.drawdown_no:
            if hasattr(self.drawdown_no, 'to_alipay_dict'):
                params['drawdown_no'] = self.drawdown_no.to_alipay_dict()
            else:
                params['drawdown_no'] = self.drawdown_no
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.site_user_id:
            if hasattr(self.site_user_id, 'to_alipay_dict'):
                params['site_user_id'] = self.site_user_id.to_alipay_dict()
            else:
                params['site_user_id'] = self.site_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodBillQueryModel()
        if 'app_seqno' in d:
            o.app_seqno = d['app_seqno']
        if 'drawdown_no' in d:
            o.drawdown_no = d['drawdown_no']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


