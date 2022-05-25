#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSupplychainWfRepaymentdetailQueryModel(object):

    def __init__(self):
        self._billno = None
        self._pagenum = None
        self._pagesize = None
        self._scene = None
        self._sellerid = None
        self._site = None
        self._siteuserid = None

    @property
    def billno(self):
        return self._billno

    @billno.setter
    def billno(self, value):
        self._billno = value
    @property
    def pagenum(self):
        return self._pagenum

    @pagenum.setter
    def pagenum(self, value):
        self._pagenum = value
    @property
    def pagesize(self):
        return self._pagesize

    @pagesize.setter
    def pagesize(self, value):
        self._pagesize = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sellerid(self):
        return self._sellerid

    @sellerid.setter
    def sellerid(self, value):
        self._sellerid = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def siteuserid(self):
        return self._siteuserid

    @siteuserid.setter
    def siteuserid(self, value):
        self._siteuserid = value


    def to_alipay_dict(self):
        params = dict()
        if self.billno:
            if hasattr(self.billno, 'to_alipay_dict'):
                params['billno'] = self.billno.to_alipay_dict()
            else:
                params['billno'] = self.billno
        if self.pagenum:
            if hasattr(self.pagenum, 'to_alipay_dict'):
                params['pagenum'] = self.pagenum.to_alipay_dict()
            else:
                params['pagenum'] = self.pagenum
        if self.pagesize:
            if hasattr(self.pagesize, 'to_alipay_dict'):
                params['pagesize'] = self.pagesize.to_alipay_dict()
            else:
                params['pagesize'] = self.pagesize
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sellerid:
            if hasattr(self.sellerid, 'to_alipay_dict'):
                params['sellerid'] = self.sellerid.to_alipay_dict()
            else:
                params['sellerid'] = self.sellerid
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.siteuserid:
            if hasattr(self.siteuserid, 'to_alipay_dict'):
                params['siteuserid'] = self.siteuserid.to_alipay_dict()
            else:
                params['siteuserid'] = self.siteuserid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainWfRepaymentdetailQueryModel()
        if 'billno' in d:
            o.billno = d['billno']
        if 'pagenum' in d:
            o.pagenum = d['pagenum']
        if 'pagesize' in d:
            o.pagesize = d['pagesize']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sellerid' in d:
            o.sellerid = d['sellerid']
        if 'site' in d:
            o.site = d['site']
        if 'siteuserid' in d:
            o.siteuserid = d['siteuserid']
        return o


