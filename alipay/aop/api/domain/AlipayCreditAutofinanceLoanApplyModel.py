#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCreditAutofinanceLoanApplyModel(object):

    def __init__(self):
        self._area = None
        self._backurl = None
        self._extparam = None
        self._itemid = None
        self._orgcode = None
        self._outorderno = None
        self._uid = None
        self._verifyid = None
        self._version = None

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def backurl(self):
        return self._backurl

    @backurl.setter
    def backurl(self, value):
        self._backurl = value
    @property
    def extparam(self):
        return self._extparam

    @extparam.setter
    def extparam(self, value):
        self._extparam = value
    @property
    def itemid(self):
        return self._itemid

    @itemid.setter
    def itemid(self, value):
        self._itemid = value
    @property
    def orgcode(self):
        return self._orgcode

    @orgcode.setter
    def orgcode(self, value):
        self._orgcode = value
    @property
    def outorderno(self):
        return self._outorderno

    @outorderno.setter
    def outorderno(self, value):
        self._outorderno = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def verifyid(self):
        return self._verifyid

    @verifyid.setter
    def verifyid(self, value):
        self._verifyid = value
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value


    def to_alipay_dict(self):
        params = dict()
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.backurl:
            if hasattr(self.backurl, 'to_alipay_dict'):
                params['backurl'] = self.backurl.to_alipay_dict()
            else:
                params['backurl'] = self.backurl
        if self.extparam:
            if hasattr(self.extparam, 'to_alipay_dict'):
                params['extparam'] = self.extparam.to_alipay_dict()
            else:
                params['extparam'] = self.extparam
        if self.itemid:
            if hasattr(self.itemid, 'to_alipay_dict'):
                params['itemid'] = self.itemid.to_alipay_dict()
            else:
                params['itemid'] = self.itemid
        if self.orgcode:
            if hasattr(self.orgcode, 'to_alipay_dict'):
                params['orgcode'] = self.orgcode.to_alipay_dict()
            else:
                params['orgcode'] = self.orgcode
        if self.outorderno:
            if hasattr(self.outorderno, 'to_alipay_dict'):
                params['outorderno'] = self.outorderno.to_alipay_dict()
            else:
                params['outorderno'] = self.outorderno
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.verifyid:
            if hasattr(self.verifyid, 'to_alipay_dict'):
                params['verifyid'] = self.verifyid.to_alipay_dict()
            else:
                params['verifyid'] = self.verifyid
        if self.version:
            if hasattr(self.version, 'to_alipay_dict'):
                params['version'] = self.version.to_alipay_dict()
            else:
                params['version'] = self.version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCreditAutofinanceLoanApplyModel()
        if 'area' in d:
            o.area = d['area']
        if 'backurl' in d:
            o.backurl = d['backurl']
        if 'extparam' in d:
            o.extparam = d['extparam']
        if 'itemid' in d:
            o.itemid = d['itemid']
        if 'orgcode' in d:
            o.orgcode = d['orgcode']
        if 'outorderno' in d:
            o.outorderno = d['outorderno']
        if 'uid' in d:
            o.uid = d['uid']
        if 'verifyid' in d:
            o.verifyid = d['verifyid']
        if 'version' in d:
            o.version = d['version']
        return o


