#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyAmountGetModel(object):

    def __init__(self):
        self._biztype = None
        self._enddate = None
        self._extinfo = None
        self._gainamount = None
        self._operatesource = None
        self._requestid = None
        self._scene = None
        self._site = None
        self._siteuserid = None
        self._startdate = None
        self._subbiztype = None

    @property
    def biztype(self):
        return self._biztype

    @biztype.setter
    def biztype(self, value):
        self._biztype = value
    @property
    def enddate(self):
        return self._enddate

    @enddate.setter
    def enddate(self, value):
        self._enddate = value
    @property
    def extinfo(self):
        return self._extinfo

    @extinfo.setter
    def extinfo(self, value):
        self._extinfo = value
    @property
    def gainamount(self):
        return self._gainamount

    @gainamount.setter
    def gainamount(self, value):
        self._gainamount = value
    @property
    def operatesource(self):
        return self._operatesource

    @operatesource.setter
    def operatesource(self, value):
        self._operatesource = value
    @property
    def requestid(self):
        return self._requestid

    @requestid.setter
    def requestid(self, value):
        self._requestid = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
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
    def startdate(self):
        return self._startdate

    @startdate.setter
    def startdate(self, value):
        self._startdate = value
    @property
    def subbiztype(self):
        return self._subbiztype

    @subbiztype.setter
    def subbiztype(self, value):
        self._subbiztype = value


    def to_alipay_dict(self):
        params = dict()
        if self.biztype:
            if hasattr(self.biztype, 'to_alipay_dict'):
                params['biztype'] = self.biztype.to_alipay_dict()
            else:
                params['biztype'] = self.biztype
        if self.enddate:
            if hasattr(self.enddate, 'to_alipay_dict'):
                params['enddate'] = self.enddate.to_alipay_dict()
            else:
                params['enddate'] = self.enddate
        if self.extinfo:
            if hasattr(self.extinfo, 'to_alipay_dict'):
                params['extinfo'] = self.extinfo.to_alipay_dict()
            else:
                params['extinfo'] = self.extinfo
        if self.gainamount:
            if hasattr(self.gainamount, 'to_alipay_dict'):
                params['gainamount'] = self.gainamount.to_alipay_dict()
            else:
                params['gainamount'] = self.gainamount
        if self.operatesource:
            if hasattr(self.operatesource, 'to_alipay_dict'):
                params['operatesource'] = self.operatesource.to_alipay_dict()
            else:
                params['operatesource'] = self.operatesource
        if self.requestid:
            if hasattr(self.requestid, 'to_alipay_dict'):
                params['requestid'] = self.requestid.to_alipay_dict()
            else:
                params['requestid'] = self.requestid
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        if self.startdate:
            if hasattr(self.startdate, 'to_alipay_dict'):
                params['startdate'] = self.startdate.to_alipay_dict()
            else:
                params['startdate'] = self.startdate
        if self.subbiztype:
            if hasattr(self.subbiztype, 'to_alipay_dict'):
                params['subbiztype'] = self.subbiztype.to_alipay_dict()
            else:
                params['subbiztype'] = self.subbiztype
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyAmountGetModel()
        if 'biztype' in d:
            o.biztype = d['biztype']
        if 'enddate' in d:
            o.enddate = d['enddate']
        if 'extinfo' in d:
            o.extinfo = d['extinfo']
        if 'gainamount' in d:
            o.gainamount = d['gainamount']
        if 'operatesource' in d:
            o.operatesource = d['operatesource']
        if 'requestid' in d:
            o.requestid = d['requestid']
        if 'scene' in d:
            o.scene = d['scene']
        if 'site' in d:
            o.site = d['site']
        if 'siteuserid' in d:
            o.siteuserid = d['siteuserid']
        if 'startdate' in d:
            o.startdate = d['startdate']
        if 'subbiztype' in d:
            o.subbiztype = d['subbiztype']
        return o


