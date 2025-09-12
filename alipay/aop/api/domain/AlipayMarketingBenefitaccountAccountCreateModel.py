#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FsAuthorizationInfoForm import FsAuthorizationInfoForm
from alipay.aop.api.domain.FsFundInfoForm import FsFundInfoForm
from alipay.aop.api.domain.FsFundRelationGroupForm import FsFundRelationGroupForm


class AlipayMarketingBenefitaccountAccountCreateModel(object):

    def __init__(self):
        self._authorization_info = None
        self._biz_from = None
        self._biz_identity = None
        self._biz_no = None
        self._effective_time = None
        self._expired_time = None
        self._fund_infos = None
        self._fund_relation_groups = None
        self._mnotify_url = None
        self._name = None
        self._publisher_user_id = None
        self._verify_id = None

    @property
    def authorization_info(self):
        return self._authorization_info

    @authorization_info.setter
    def authorization_info(self, value):
        if isinstance(value, FsAuthorizationInfoForm):
            self._authorization_info = value
        else:
            self._authorization_info = FsAuthorizationInfoForm.from_alipay_dict(value)
    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def fund_infos(self):
        return self._fund_infos

    @fund_infos.setter
    def fund_infos(self, value):
        if isinstance(value, list):
            self._fund_infos = list()
            for i in value:
                if isinstance(i, FsFundInfoForm):
                    self._fund_infos.append(i)
                else:
                    self._fund_infos.append(FsFundInfoForm.from_alipay_dict(i))
    @property
    def fund_relation_groups(self):
        return self._fund_relation_groups

    @fund_relation_groups.setter
    def fund_relation_groups(self, value):
        if isinstance(value, list):
            self._fund_relation_groups = list()
            for i in value:
                if isinstance(i, FsFundRelationGroupForm):
                    self._fund_relation_groups.append(i)
                else:
                    self._fund_relation_groups.append(FsFundRelationGroupForm.from_alipay_dict(i))
    @property
    def mnotify_url(self):
        return self._mnotify_url

    @mnotify_url.setter
    def mnotify_url(self, value):
        self._mnotify_url = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def publisher_user_id(self):
        return self._publisher_user_id

    @publisher_user_id.setter
    def publisher_user_id(self, value):
        self._publisher_user_id = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorization_info:
            if hasattr(self.authorization_info, 'to_alipay_dict'):
                params['authorization_info'] = self.authorization_info.to_alipay_dict()
            else:
                params['authorization_info'] = self.authorization_info
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.biz_identity:
            if hasattr(self.biz_identity, 'to_alipay_dict'):
                params['biz_identity'] = self.biz_identity.to_alipay_dict()
            else:
                params['biz_identity'] = self.biz_identity
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.fund_infos:
            if isinstance(self.fund_infos, list):
                for i in range(0, len(self.fund_infos)):
                    element = self.fund_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_infos[i] = element.to_alipay_dict()
            if hasattr(self.fund_infos, 'to_alipay_dict'):
                params['fund_infos'] = self.fund_infos.to_alipay_dict()
            else:
                params['fund_infos'] = self.fund_infos
        if self.fund_relation_groups:
            if isinstance(self.fund_relation_groups, list):
                for i in range(0, len(self.fund_relation_groups)):
                    element = self.fund_relation_groups[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_relation_groups[i] = element.to_alipay_dict()
            if hasattr(self.fund_relation_groups, 'to_alipay_dict'):
                params['fund_relation_groups'] = self.fund_relation_groups.to_alipay_dict()
            else:
                params['fund_relation_groups'] = self.fund_relation_groups
        if self.mnotify_url:
            if hasattr(self.mnotify_url, 'to_alipay_dict'):
                params['mnotify_url'] = self.mnotify_url.to_alipay_dict()
            else:
                params['mnotify_url'] = self.mnotify_url
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.publisher_user_id:
            if hasattr(self.publisher_user_id, 'to_alipay_dict'):
                params['publisher_user_id'] = self.publisher_user_id.to_alipay_dict()
            else:
                params['publisher_user_id'] = self.publisher_user_id
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingBenefitaccountAccountCreateModel()
        if 'authorization_info' in d:
            o.authorization_info = d['authorization_info']
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'biz_identity' in d:
            o.biz_identity = d['biz_identity']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'fund_infos' in d:
            o.fund_infos = d['fund_infos']
        if 'fund_relation_groups' in d:
            o.fund_relation_groups = d['fund_relation_groups']
        if 'mnotify_url' in d:
            o.mnotify_url = d['mnotify_url']
        if 'name' in d:
            o.name = d['name']
        if 'publisher_user_id' in d:
            o.publisher_user_id = d['publisher_user_id']
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        return o


