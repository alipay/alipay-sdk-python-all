#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCreditCreditriskDataPutModel(object):

    def __init__(self):
        self._category = None
        self._dataorgid = None
        self._dataprovider = None
        self._entitycode = None
        self._entityname = None
        self._entitytype = None
        self._mybk_auth_scene_code = None
        self._mybk_auth_token = None
        self._objectcontent = None
        self._openid = None
        self._taskid = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def dataorgid(self):
        return self._dataorgid

    @dataorgid.setter
    def dataorgid(self, value):
        self._dataorgid = value
    @property
    def dataprovider(self):
        return self._dataprovider

    @dataprovider.setter
    def dataprovider(self, value):
        self._dataprovider = value
    @property
    def entitycode(self):
        return self._entitycode

    @entitycode.setter
    def entitycode(self, value):
        self._entitycode = value
    @property
    def entityname(self):
        return self._entityname

    @entityname.setter
    def entityname(self, value):
        self._entityname = value
    @property
    def entitytype(self):
        return self._entitytype

    @entitytype.setter
    def entitytype(self, value):
        self._entitytype = value
    @property
    def mybk_auth_scene_code(self):
        return self._mybk_auth_scene_code

    @mybk_auth_scene_code.setter
    def mybk_auth_scene_code(self, value):
        self._mybk_auth_scene_code = value
    @property
    def mybk_auth_token(self):
        return self._mybk_auth_token

    @mybk_auth_token.setter
    def mybk_auth_token(self, value):
        self._mybk_auth_token = value
    @property
    def objectcontent(self):
        return self._objectcontent

    @objectcontent.setter
    def objectcontent(self, value):
        self._objectcontent = value
    @property
    def openid(self):
        return self._openid

    @openid.setter
    def openid(self, value):
        self._openid = value
    @property
    def taskid(self):
        return self._taskid

    @taskid.setter
    def taskid(self, value):
        self._taskid = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.dataorgid:
            if hasattr(self.dataorgid, 'to_alipay_dict'):
                params['dataorgid'] = self.dataorgid.to_alipay_dict()
            else:
                params['dataorgid'] = self.dataorgid
        if self.dataprovider:
            if hasattr(self.dataprovider, 'to_alipay_dict'):
                params['dataprovider'] = self.dataprovider.to_alipay_dict()
            else:
                params['dataprovider'] = self.dataprovider
        if self.entitycode:
            if hasattr(self.entitycode, 'to_alipay_dict'):
                params['entitycode'] = self.entitycode.to_alipay_dict()
            else:
                params['entitycode'] = self.entitycode
        if self.entityname:
            if hasattr(self.entityname, 'to_alipay_dict'):
                params['entityname'] = self.entityname.to_alipay_dict()
            else:
                params['entityname'] = self.entityname
        if self.entitytype:
            if hasattr(self.entitytype, 'to_alipay_dict'):
                params['entitytype'] = self.entitytype.to_alipay_dict()
            else:
                params['entitytype'] = self.entitytype
        if self.mybk_auth_scene_code:
            if hasattr(self.mybk_auth_scene_code, 'to_alipay_dict'):
                params['mybk_auth_scene_code'] = self.mybk_auth_scene_code.to_alipay_dict()
            else:
                params['mybk_auth_scene_code'] = self.mybk_auth_scene_code
        if self.mybk_auth_token:
            if hasattr(self.mybk_auth_token, 'to_alipay_dict'):
                params['mybk_auth_token'] = self.mybk_auth_token.to_alipay_dict()
            else:
                params['mybk_auth_token'] = self.mybk_auth_token
        if self.objectcontent:
            if hasattr(self.objectcontent, 'to_alipay_dict'):
                params['objectcontent'] = self.objectcontent.to_alipay_dict()
            else:
                params['objectcontent'] = self.objectcontent
        if self.openid:
            if hasattr(self.openid, 'to_alipay_dict'):
                params['openid'] = self.openid.to_alipay_dict()
            else:
                params['openid'] = self.openid
        if self.taskid:
            if hasattr(self.taskid, 'to_alipay_dict'):
                params['taskid'] = self.taskid.to_alipay_dict()
            else:
                params['taskid'] = self.taskid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCreditCreditriskDataPutModel()
        if 'category' in d:
            o.category = d['category']
        if 'dataorgid' in d:
            o.dataorgid = d['dataorgid']
        if 'dataprovider' in d:
            o.dataprovider = d['dataprovider']
        if 'entitycode' in d:
            o.entitycode = d['entitycode']
        if 'entityname' in d:
            o.entityname = d['entityname']
        if 'entitytype' in d:
            o.entitytype = d['entitytype']
        if 'mybk_auth_scene_code' in d:
            o.mybk_auth_scene_code = d['mybk_auth_scene_code']
        if 'mybk_auth_token' in d:
            o.mybk_auth_token = d['mybk_auth_token']
        if 'objectcontent' in d:
            o.objectcontent = d['objectcontent']
        if 'openid' in d:
            o.openid = d['openid']
        if 'taskid' in d:
            o.taskid = d['taskid']
        return o


