#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MemberActionModel import MemberActionModel
from alipay.aop.api.domain.MemberAssetModel import MemberAssetModel
from alipay.aop.api.domain.MemberBenefitModel import MemberBenefitModel
from alipay.aop.api.domain.MemberLevelModel import MemberLevelModel
from alipay.aop.api.domain.MemberOpenInfoModel import MemberOpenInfoModel


class KoubeiMarketingCampaignMemberTemplateCreateModel(object):

    def __init__(self):
        self._client_channels = None
        self._desc = None
        self._member_actions = None
        self._member_assets = None
        self._member_benefits = None
        self._member_levels = None
        self._member_open_info = None
        self._name = None
        self._out_template_id = None
        self._request_id = None
        self._write_off_type = None

    @property
    def client_channels(self):
        return self._client_channels

    @client_channels.setter
    def client_channels(self, value):
        if isinstance(value, list):
            self._client_channels = list()
            for i in value:
                self._client_channels.append(i)
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def member_actions(self):
        return self._member_actions

    @member_actions.setter
    def member_actions(self, value):
        if isinstance(value, list):
            self._member_actions = list()
            for i in value:
                if isinstance(i, MemberActionModel):
                    self._member_actions.append(i)
                else:
                    self._member_actions.append(MemberActionModel.from_alipay_dict(i))
    @property
    def member_assets(self):
        return self._member_assets

    @member_assets.setter
    def member_assets(self, value):
        if isinstance(value, list):
            self._member_assets = list()
            for i in value:
                if isinstance(i, MemberAssetModel):
                    self._member_assets.append(i)
                else:
                    self._member_assets.append(MemberAssetModel.from_alipay_dict(i))
    @property
    def member_benefits(self):
        return self._member_benefits

    @member_benefits.setter
    def member_benefits(self, value):
        if isinstance(value, list):
            self._member_benefits = list()
            for i in value:
                if isinstance(i, MemberBenefitModel):
                    self._member_benefits.append(i)
                else:
                    self._member_benefits.append(MemberBenefitModel.from_alipay_dict(i))
    @property
    def member_levels(self):
        return self._member_levels

    @member_levels.setter
    def member_levels(self, value):
        if isinstance(value, list):
            self._member_levels = list()
            for i in value:
                if isinstance(i, MemberLevelModel):
                    self._member_levels.append(i)
                else:
                    self._member_levels.append(MemberLevelModel.from_alipay_dict(i))
    @property
    def member_open_info(self):
        return self._member_open_info

    @member_open_info.setter
    def member_open_info(self, value):
        if isinstance(value, MemberOpenInfoModel):
            self._member_open_info = value
        else:
            self._member_open_info = MemberOpenInfoModel.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_template_id(self):
        return self._out_template_id

    @out_template_id.setter
    def out_template_id(self, value):
        self._out_template_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def write_off_type(self):
        return self._write_off_type

    @write_off_type.setter
    def write_off_type(self, value):
        self._write_off_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_channels:
            if isinstance(self.client_channels, list):
                for i in range(0, len(self.client_channels)):
                    element = self.client_channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.client_channels[i] = element.to_alipay_dict()
            if hasattr(self.client_channels, 'to_alipay_dict'):
                params['client_channels'] = self.client_channels.to_alipay_dict()
            else:
                params['client_channels'] = self.client_channels
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.member_actions:
            if isinstance(self.member_actions, list):
                for i in range(0, len(self.member_actions)):
                    element = self.member_actions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.member_actions[i] = element.to_alipay_dict()
            if hasattr(self.member_actions, 'to_alipay_dict'):
                params['member_actions'] = self.member_actions.to_alipay_dict()
            else:
                params['member_actions'] = self.member_actions
        if self.member_assets:
            if isinstance(self.member_assets, list):
                for i in range(0, len(self.member_assets)):
                    element = self.member_assets[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.member_assets[i] = element.to_alipay_dict()
            if hasattr(self.member_assets, 'to_alipay_dict'):
                params['member_assets'] = self.member_assets.to_alipay_dict()
            else:
                params['member_assets'] = self.member_assets
        if self.member_benefits:
            if isinstance(self.member_benefits, list):
                for i in range(0, len(self.member_benefits)):
                    element = self.member_benefits[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.member_benefits[i] = element.to_alipay_dict()
            if hasattr(self.member_benefits, 'to_alipay_dict'):
                params['member_benefits'] = self.member_benefits.to_alipay_dict()
            else:
                params['member_benefits'] = self.member_benefits
        if self.member_levels:
            if isinstance(self.member_levels, list):
                for i in range(0, len(self.member_levels)):
                    element = self.member_levels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.member_levels[i] = element.to_alipay_dict()
            if hasattr(self.member_levels, 'to_alipay_dict'):
                params['member_levels'] = self.member_levels.to_alipay_dict()
            else:
                params['member_levels'] = self.member_levels
        if self.member_open_info:
            if hasattr(self.member_open_info, 'to_alipay_dict'):
                params['member_open_info'] = self.member_open_info.to_alipay_dict()
            else:
                params['member_open_info'] = self.member_open_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_template_id:
            if hasattr(self.out_template_id, 'to_alipay_dict'):
                params['out_template_id'] = self.out_template_id.to_alipay_dict()
            else:
                params['out_template_id'] = self.out_template_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.write_off_type:
            if hasattr(self.write_off_type, 'to_alipay_dict'):
                params['write_off_type'] = self.write_off_type.to_alipay_dict()
            else:
                params['write_off_type'] = self.write_off_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignMemberTemplateCreateModel()
        if 'client_channels' in d:
            o.client_channels = d['client_channels']
        if 'desc' in d:
            o.desc = d['desc']
        if 'member_actions' in d:
            o.member_actions = d['member_actions']
        if 'member_assets' in d:
            o.member_assets = d['member_assets']
        if 'member_benefits' in d:
            o.member_benefits = d['member_benefits']
        if 'member_levels' in d:
            o.member_levels = d['member_levels']
        if 'member_open_info' in d:
            o.member_open_info = d['member_open_info']
        if 'name' in d:
            o.name = d['name']
        if 'out_template_id' in d:
            o.out_template_id = d['out_template_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'write_off_type' in d:
            o.write_off_type = d['write_off_type']
        return o


