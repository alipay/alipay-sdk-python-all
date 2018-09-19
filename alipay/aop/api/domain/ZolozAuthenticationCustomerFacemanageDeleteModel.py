#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozAuthenticationCustomerFacemanageDeleteModel(object):

    def __init__(self):
        self._areacode = None
        self._biz_type = None
        self._bizscale = None
        self._brandcode = None
        self._devicenum = None
        self._extinfo = None
        self._facetype = None
        self._faceval = None
        self._group = None
        self._storecode = None
        self._validtimes = None

    @property
    def areacode(self):
        return self._areacode

    @areacode.setter
    def areacode(self, value):
        self._areacode = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def bizscale(self):
        return self._bizscale

    @bizscale.setter
    def bizscale(self, value):
        self._bizscale = value
    @property
    def brandcode(self):
        return self._brandcode

    @brandcode.setter
    def brandcode(self, value):
        self._brandcode = value
    @property
    def devicenum(self):
        return self._devicenum

    @devicenum.setter
    def devicenum(self, value):
        self._devicenum = value
    @property
    def extinfo(self):
        return self._extinfo

    @extinfo.setter
    def extinfo(self, value):
        self._extinfo = value
    @property
    def facetype(self):
        return self._facetype

    @facetype.setter
    def facetype(self, value):
        self._facetype = value
    @property
    def faceval(self):
        return self._faceval

    @faceval.setter
    def faceval(self, value):
        self._faceval = value
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value
    @property
    def storecode(self):
        return self._storecode

    @storecode.setter
    def storecode(self, value):
        self._storecode = value
    @property
    def validtimes(self):
        return self._validtimes

    @validtimes.setter
    def validtimes(self, value):
        self._validtimes = value


    def to_alipay_dict(self):
        params = dict()
        if self.areacode:
            if hasattr(self.areacode, 'to_alipay_dict'):
                params['areacode'] = self.areacode.to_alipay_dict()
            else:
                params['areacode'] = self.areacode
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.bizscale:
            if hasattr(self.bizscale, 'to_alipay_dict'):
                params['bizscale'] = self.bizscale.to_alipay_dict()
            else:
                params['bizscale'] = self.bizscale
        if self.brandcode:
            if hasattr(self.brandcode, 'to_alipay_dict'):
                params['brandcode'] = self.brandcode.to_alipay_dict()
            else:
                params['brandcode'] = self.brandcode
        if self.devicenum:
            if hasattr(self.devicenum, 'to_alipay_dict'):
                params['devicenum'] = self.devicenum.to_alipay_dict()
            else:
                params['devicenum'] = self.devicenum
        if self.extinfo:
            if hasattr(self.extinfo, 'to_alipay_dict'):
                params['extinfo'] = self.extinfo.to_alipay_dict()
            else:
                params['extinfo'] = self.extinfo
        if self.facetype:
            if hasattr(self.facetype, 'to_alipay_dict'):
                params['facetype'] = self.facetype.to_alipay_dict()
            else:
                params['facetype'] = self.facetype
        if self.faceval:
            if hasattr(self.faceval, 'to_alipay_dict'):
                params['faceval'] = self.faceval.to_alipay_dict()
            else:
                params['faceval'] = self.faceval
        if self.group:
            if hasattr(self.group, 'to_alipay_dict'):
                params['group'] = self.group.to_alipay_dict()
            else:
                params['group'] = self.group
        if self.storecode:
            if hasattr(self.storecode, 'to_alipay_dict'):
                params['storecode'] = self.storecode.to_alipay_dict()
            else:
                params['storecode'] = self.storecode
        if self.validtimes:
            if hasattr(self.validtimes, 'to_alipay_dict'):
                params['validtimes'] = self.validtimes.to_alipay_dict()
            else:
                params['validtimes'] = self.validtimes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationCustomerFacemanageDeleteModel()
        if 'areacode' in d:
            o.areacode = d['areacode']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'bizscale' in d:
            o.bizscale = d['bizscale']
        if 'brandcode' in d:
            o.brandcode = d['brandcode']
        if 'devicenum' in d:
            o.devicenum = d['devicenum']
        if 'extinfo' in d:
            o.extinfo = d['extinfo']
        if 'facetype' in d:
            o.facetype = d['facetype']
        if 'faceval' in d:
            o.faceval = d['faceval']
        if 'group' in d:
            o.group = d['group']
        if 'storecode' in d:
            o.storecode = d['storecode']
        if 'validtimes' in d:
            o.validtimes = d['validtimes']
        return o


