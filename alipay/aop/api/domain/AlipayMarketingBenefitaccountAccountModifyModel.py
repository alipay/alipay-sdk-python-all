#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FsFundInfoForm import FsFundInfoForm
from alipay.aop.api.domain.FsFundRelationGroupForm import FsFundRelationGroupForm


class AlipayMarketingBenefitaccountAccountModifyModel(object):

    def __init__(self):
        self._benefit_account_no = None
        self._biz_no = None
        self._fund_infos = None
        self._fund_relation_groups = None
        self._publisher_user_id = None

    @property
    def benefit_account_no(self):
        return self._benefit_account_no

    @benefit_account_no.setter
    def benefit_account_no(self, value):
        self._benefit_account_no = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
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
    def publisher_user_id(self):
        return self._publisher_user_id

    @publisher_user_id.setter
    def publisher_user_id(self, value):
        self._publisher_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_account_no:
            if hasattr(self.benefit_account_no, 'to_alipay_dict'):
                params['benefit_account_no'] = self.benefit_account_no.to_alipay_dict()
            else:
                params['benefit_account_no'] = self.benefit_account_no
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
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
        if self.publisher_user_id:
            if hasattr(self.publisher_user_id, 'to_alipay_dict'):
                params['publisher_user_id'] = self.publisher_user_id.to_alipay_dict()
            else:
                params['publisher_user_id'] = self.publisher_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingBenefitaccountAccountModifyModel()
        if 'benefit_account_no' in d:
            o.benefit_account_no = d['benefit_account_no']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'fund_infos' in d:
            o.fund_infos = d['fund_infos']
        if 'fund_relation_groups' in d:
            o.fund_relation_groups = d['fund_relation_groups']
        if 'publisher_user_id' in d:
            o.publisher_user_id = d['publisher_user_id']
        return o


