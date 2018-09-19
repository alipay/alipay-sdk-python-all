#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignRuleRulelistQueryModel(object):

    def __init__(self):
        self._mpid = None
        self._pageno = None
        self._pagesize = None

    @property
    def mpid(self):
        return self._mpid

    @mpid.setter
    def mpid(self, value):
        self._mpid = value
    @property
    def pageno(self):
        return self._pageno

    @pageno.setter
    def pageno(self, value):
        self._pageno = value
    @property
    def pagesize(self):
        return self._pagesize

    @pagesize.setter
    def pagesize(self, value):
        self._pagesize = value


    def to_alipay_dict(self):
        params = dict()
        if self.mpid:
            if hasattr(self.mpid, 'to_alipay_dict'):
                params['mpid'] = self.mpid.to_alipay_dict()
            else:
                params['mpid'] = self.mpid
        if self.pageno:
            if hasattr(self.pageno, 'to_alipay_dict'):
                params['pageno'] = self.pageno.to_alipay_dict()
            else:
                params['pageno'] = self.pageno
        if self.pagesize:
            if hasattr(self.pagesize, 'to_alipay_dict'):
                params['pagesize'] = self.pagesize.to_alipay_dict()
            else:
                params['pagesize'] = self.pagesize
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignRuleRulelistQueryModel()
        if 'mpid' in d:
            o.mpid = d['mpid']
        if 'pageno' in d:
            o.pageno = d['pageno']
        if 'pagesize' in d:
            o.pagesize = d['pagesize']
        return o


