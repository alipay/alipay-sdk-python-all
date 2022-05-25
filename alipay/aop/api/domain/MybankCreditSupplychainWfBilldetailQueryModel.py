#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSupplychainWfBilldetailQueryModel(object):

    def __init__(self):
        self._maxstartdate = None
        self._minstartdate = None
        self._pagenum = None
        self._pagesize = None
        self._scene = None
        self._sellerid = None
        self._site = None
        self._siteuserid = None
        self._status = None

    @property
    def maxstartdate(self):
        return self._maxstartdate

    @maxstartdate.setter
    def maxstartdate(self, value):
        self._maxstartdate = value
    @property
    def minstartdate(self):
        return self._minstartdate

    @minstartdate.setter
    def minstartdate(self, value):
        self._minstartdate = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.maxstartdate:
            if hasattr(self.maxstartdate, 'to_alipay_dict'):
                params['maxstartdate'] = self.maxstartdate.to_alipay_dict()
            else:
                params['maxstartdate'] = self.maxstartdate
        if self.minstartdate:
            if hasattr(self.minstartdate, 'to_alipay_dict'):
                params['minstartdate'] = self.minstartdate.to_alipay_dict()
            else:
                params['minstartdate'] = self.minstartdate
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
        o = MybankCreditSupplychainWfBilldetailQueryModel()
        if 'maxstartdate' in d:
            o.maxstartdate = d['maxstartdate']
        if 'minstartdate' in d:
            o.minstartdate = d['minstartdate']
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
        if 'status' in d:
            o.status = d['status']
        return o


