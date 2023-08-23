#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RcvApproverDto(object):

    def __init__(self):
        self._asset_manager = None
        self._financial_review = None
        self._financial_super = None
        self._requester = None
        self._requester_supervisor = None
        self._specify_asset_manager = None
        self._specify_requester = None

    @property
    def asset_manager(self):
        return self._asset_manager

    @asset_manager.setter
    def asset_manager(self, value):
        if isinstance(value, list):
            self._asset_manager = list()
            for i in value:
                self._asset_manager.append(i)
    @property
    def financial_review(self):
        return self._financial_review

    @financial_review.setter
    def financial_review(self, value):
        if isinstance(value, list):
            self._financial_review = list()
            for i in value:
                self._financial_review.append(i)
    @property
    def financial_super(self):
        return self._financial_super

    @financial_super.setter
    def financial_super(self, value):
        if isinstance(value, list):
            self._financial_super = list()
            for i in value:
                self._financial_super.append(i)
    @property
    def requester(self):
        return self._requester

    @requester.setter
    def requester(self, value):
        if isinstance(value, list):
            self._requester = list()
            for i in value:
                self._requester.append(i)
    @property
    def requester_supervisor(self):
        return self._requester_supervisor

    @requester_supervisor.setter
    def requester_supervisor(self, value):
        if isinstance(value, list):
            self._requester_supervisor = list()
            for i in value:
                self._requester_supervisor.append(i)
    @property
    def specify_asset_manager(self):
        return self._specify_asset_manager

    @specify_asset_manager.setter
    def specify_asset_manager(self, value):
        if isinstance(value, list):
            self._specify_asset_manager = list()
            for i in value:
                self._specify_asset_manager.append(i)
    @property
    def specify_requester(self):
        return self._specify_requester

    @specify_requester.setter
    def specify_requester(self, value):
        if isinstance(value, list):
            self._specify_requester = list()
            for i in value:
                self._specify_requester.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.asset_manager:
            if isinstance(self.asset_manager, list):
                for i in range(0, len(self.asset_manager)):
                    element = self.asset_manager[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_manager[i] = element.to_alipay_dict()
            if hasattr(self.asset_manager, 'to_alipay_dict'):
                params['asset_manager'] = self.asset_manager.to_alipay_dict()
            else:
                params['asset_manager'] = self.asset_manager
        if self.financial_review:
            if isinstance(self.financial_review, list):
                for i in range(0, len(self.financial_review)):
                    element = self.financial_review[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.financial_review[i] = element.to_alipay_dict()
            if hasattr(self.financial_review, 'to_alipay_dict'):
                params['financial_review'] = self.financial_review.to_alipay_dict()
            else:
                params['financial_review'] = self.financial_review
        if self.financial_super:
            if isinstance(self.financial_super, list):
                for i in range(0, len(self.financial_super)):
                    element = self.financial_super[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.financial_super[i] = element.to_alipay_dict()
            if hasattr(self.financial_super, 'to_alipay_dict'):
                params['financial_super'] = self.financial_super.to_alipay_dict()
            else:
                params['financial_super'] = self.financial_super
        if self.requester:
            if isinstance(self.requester, list):
                for i in range(0, len(self.requester)):
                    element = self.requester[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.requester[i] = element.to_alipay_dict()
            if hasattr(self.requester, 'to_alipay_dict'):
                params['requester'] = self.requester.to_alipay_dict()
            else:
                params['requester'] = self.requester
        if self.requester_supervisor:
            if isinstance(self.requester_supervisor, list):
                for i in range(0, len(self.requester_supervisor)):
                    element = self.requester_supervisor[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.requester_supervisor[i] = element.to_alipay_dict()
            if hasattr(self.requester_supervisor, 'to_alipay_dict'):
                params['requester_supervisor'] = self.requester_supervisor.to_alipay_dict()
            else:
                params['requester_supervisor'] = self.requester_supervisor
        if self.specify_asset_manager:
            if isinstance(self.specify_asset_manager, list):
                for i in range(0, len(self.specify_asset_manager)):
                    element = self.specify_asset_manager[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.specify_asset_manager[i] = element.to_alipay_dict()
            if hasattr(self.specify_asset_manager, 'to_alipay_dict'):
                params['specify_asset_manager'] = self.specify_asset_manager.to_alipay_dict()
            else:
                params['specify_asset_manager'] = self.specify_asset_manager
        if self.specify_requester:
            if isinstance(self.specify_requester, list):
                for i in range(0, len(self.specify_requester)):
                    element = self.specify_requester[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.specify_requester[i] = element.to_alipay_dict()
            if hasattr(self.specify_requester, 'to_alipay_dict'):
                params['specify_requester'] = self.specify_requester.to_alipay_dict()
            else:
                params['specify_requester'] = self.specify_requester
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RcvApproverDto()
        if 'asset_manager' in d:
            o.asset_manager = d['asset_manager']
        if 'financial_review' in d:
            o.financial_review = d['financial_review']
        if 'financial_super' in d:
            o.financial_super = d['financial_super']
        if 'requester' in d:
            o.requester = d['requester']
        if 'requester_supervisor' in d:
            o.requester_supervisor = d['requester_supervisor']
        if 'specify_asset_manager' in d:
            o.specify_asset_manager = d['specify_asset_manager']
        if 'specify_requester' in d:
            o.specify_requester = d['specify_requester']
        return o


