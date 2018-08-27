#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateActionInfoDTO import TemplateActionInfoDTO
from alipay.aop.api.domain.TemplateCardLevelConfDTO import TemplateCardLevelConfDTO
from alipay.aop.api.domain.TemplateColumnInfoDTO import TemplateColumnInfoDTO
from alipay.aop.api.domain.TemplateFieldRuleDTO import TemplateFieldRuleDTO
from alipay.aop.api.domain.TemplateMdcodeNotifyConfDTO import TemplateMdcodeNotifyConfDTO
from alipay.aop.api.domain.TemplateOpenCardConfDTO import TemplateOpenCardConfDTO
from alipay.aop.api.domain.PubChannelDTO import PubChannelDTO
from alipay.aop.api.domain.TemplateBenefitInfoDTO import TemplateBenefitInfoDTO
from alipay.aop.api.domain.TemplateStyleInfoDTO import TemplateStyleInfoDTO


class AlipayMarketingCardTemplateModifyModel(object):

    def __init__(self):
        self._biz_no_prefix = None
        self._card_action_list = None
        self._card_level_conf = None
        self._card_spec_tag = None
        self._column_info_list = None
        self._field_rule_list = None
        self._mdcode_notify_conf = None
        self._open_card_conf = None
        self._pub_channels = None
        self._request_id = None
        self._shop_ids = None
        self._template_benefit_info = None
        self._template_id = None
        self._template_style_info = None
        self._write_off_type = None

    @property
    def biz_no_prefix(self):
        return self._biz_no_prefix

    @biz_no_prefix.setter
    def biz_no_prefix(self, value):
        self._biz_no_prefix = value
    @property
    def card_action_list(self):
        return self._card_action_list

    @card_action_list.setter
    def card_action_list(self, value):
        if isinstance(value, list):
            self._card_action_list = list()
            for i in value:
                if isinstance(i, TemplateActionInfoDTO):
                    self._card_action_list.append(i)
                else:
                    self._card_action_list.append(TemplateActionInfoDTO.from_alipay_dict(i))
    @property
    def card_level_conf(self):
        return self._card_level_conf

    @card_level_conf.setter
    def card_level_conf(self, value):
        if isinstance(value, list):
            self._card_level_conf = list()
            for i in value:
                if isinstance(i, TemplateCardLevelConfDTO):
                    self._card_level_conf.append(i)
                else:
                    self._card_level_conf.append(TemplateCardLevelConfDTO.from_alipay_dict(i))
    @property
    def card_spec_tag(self):
        return self._card_spec_tag

    @card_spec_tag.setter
    def card_spec_tag(self, value):
        self._card_spec_tag = value
    @property
    def column_info_list(self):
        return self._column_info_list

    @column_info_list.setter
    def column_info_list(self, value):
        if isinstance(value, list):
            self._column_info_list = list()
            for i in value:
                if isinstance(i, TemplateColumnInfoDTO):
                    self._column_info_list.append(i)
                else:
                    self._column_info_list.append(TemplateColumnInfoDTO.from_alipay_dict(i))
    @property
    def field_rule_list(self):
        return self._field_rule_list

    @field_rule_list.setter
    def field_rule_list(self, value):
        if isinstance(value, list):
            self._field_rule_list = list()
            for i in value:
                if isinstance(i, TemplateFieldRuleDTO):
                    self._field_rule_list.append(i)
                else:
                    self._field_rule_list.append(TemplateFieldRuleDTO.from_alipay_dict(i))
    @property
    def mdcode_notify_conf(self):
        return self._mdcode_notify_conf

    @mdcode_notify_conf.setter
    def mdcode_notify_conf(self, value):
        if isinstance(value, TemplateMdcodeNotifyConfDTO):
            self._mdcode_notify_conf = value
        else:
            self._mdcode_notify_conf = TemplateMdcodeNotifyConfDTO.from_alipay_dict(value)
    @property
    def open_card_conf(self):
        return self._open_card_conf

    @open_card_conf.setter
    def open_card_conf(self, value):
        if isinstance(value, TemplateOpenCardConfDTO):
            self._open_card_conf = value
        else:
            self._open_card_conf = TemplateOpenCardConfDTO.from_alipay_dict(value)
    @property
    def pub_channels(self):
        return self._pub_channels

    @pub_channels.setter
    def pub_channels(self, value):
        if isinstance(value, list):
            self._pub_channels = list()
            for i in value:
                if isinstance(i, PubChannelDTO):
                    self._pub_channels.append(i)
                else:
                    self._pub_channels.append(PubChannelDTO.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)
    @property
    def template_benefit_info(self):
        return self._template_benefit_info

    @template_benefit_info.setter
    def template_benefit_info(self, value):
        if isinstance(value, list):
            self._template_benefit_info = list()
            for i in value:
                if isinstance(i, TemplateBenefitInfoDTO):
                    self._template_benefit_info.append(i)
                else:
                    self._template_benefit_info.append(TemplateBenefitInfoDTO.from_alipay_dict(i))
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_style_info(self):
        return self._template_style_info

    @template_style_info.setter
    def template_style_info(self, value):
        if isinstance(value, TemplateStyleInfoDTO):
            self._template_style_info = value
        else:
            self._template_style_info = TemplateStyleInfoDTO.from_alipay_dict(value)
    @property
    def write_off_type(self):
        return self._write_off_type

    @write_off_type.setter
    def write_off_type(self, value):
        self._write_off_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no_prefix:
            if hasattr(self.biz_no_prefix, 'to_alipay_dict'):
                params['biz_no_prefix'] = self.biz_no_prefix.to_alipay_dict()
            else:
                params['biz_no_prefix'] = self.biz_no_prefix
        if self.card_action_list:
            if isinstance(self.card_action_list, list):
                for i in range(0, len(self.card_action_list)):
                    element = self.card_action_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_action_list[i] = element.to_alipay_dict()
            if hasattr(self.card_action_list, 'to_alipay_dict'):
                params['card_action_list'] = self.card_action_list.to_alipay_dict()
            else:
                params['card_action_list'] = self.card_action_list
        if self.card_level_conf:
            if isinstance(self.card_level_conf, list):
                for i in range(0, len(self.card_level_conf)):
                    element = self.card_level_conf[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_level_conf[i] = element.to_alipay_dict()
            if hasattr(self.card_level_conf, 'to_alipay_dict'):
                params['card_level_conf'] = self.card_level_conf.to_alipay_dict()
            else:
                params['card_level_conf'] = self.card_level_conf
        if self.card_spec_tag:
            if hasattr(self.card_spec_tag, 'to_alipay_dict'):
                params['card_spec_tag'] = self.card_spec_tag.to_alipay_dict()
            else:
                params['card_spec_tag'] = self.card_spec_tag
        if self.column_info_list:
            if isinstance(self.column_info_list, list):
                for i in range(0, len(self.column_info_list)):
                    element = self.column_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.column_info_list[i] = element.to_alipay_dict()
            if hasattr(self.column_info_list, 'to_alipay_dict'):
                params['column_info_list'] = self.column_info_list.to_alipay_dict()
            else:
                params['column_info_list'] = self.column_info_list
        if self.field_rule_list:
            if isinstance(self.field_rule_list, list):
                for i in range(0, len(self.field_rule_list)):
                    element = self.field_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.field_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.field_rule_list, 'to_alipay_dict'):
                params['field_rule_list'] = self.field_rule_list.to_alipay_dict()
            else:
                params['field_rule_list'] = self.field_rule_list
        if self.mdcode_notify_conf:
            if hasattr(self.mdcode_notify_conf, 'to_alipay_dict'):
                params['mdcode_notify_conf'] = self.mdcode_notify_conf.to_alipay_dict()
            else:
                params['mdcode_notify_conf'] = self.mdcode_notify_conf
        if self.open_card_conf:
            if hasattr(self.open_card_conf, 'to_alipay_dict'):
                params['open_card_conf'] = self.open_card_conf.to_alipay_dict()
            else:
                params['open_card_conf'] = self.open_card_conf
        if self.pub_channels:
            if isinstance(self.pub_channels, list):
                for i in range(0, len(self.pub_channels)):
                    element = self.pub_channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pub_channels[i] = element.to_alipay_dict()
            if hasattr(self.pub_channels, 'to_alipay_dict'):
                params['pub_channels'] = self.pub_channels.to_alipay_dict()
            else:
                params['pub_channels'] = self.pub_channels
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.shop_ids:
            if isinstance(self.shop_ids, list):
                for i in range(0, len(self.shop_ids)):
                    element = self.shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        if self.template_benefit_info:
            if isinstance(self.template_benefit_info, list):
                for i in range(0, len(self.template_benefit_info)):
                    element = self.template_benefit_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_benefit_info[i] = element.to_alipay_dict()
            if hasattr(self.template_benefit_info, 'to_alipay_dict'):
                params['template_benefit_info'] = self.template_benefit_info.to_alipay_dict()
            else:
                params['template_benefit_info'] = self.template_benefit_info
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_style_info:
            if hasattr(self.template_style_info, 'to_alipay_dict'):
                params['template_style_info'] = self.template_style_info.to_alipay_dict()
            else:
                params['template_style_info'] = self.template_style_info
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
        o = AlipayMarketingCardTemplateModifyModel()
        if 'biz_no_prefix' in d:
            o.biz_no_prefix = d['biz_no_prefix']
        if 'card_action_list' in d:
            o.card_action_list = d['card_action_list']
        if 'card_level_conf' in d:
            o.card_level_conf = d['card_level_conf']
        if 'card_spec_tag' in d:
            o.card_spec_tag = d['card_spec_tag']
        if 'column_info_list' in d:
            o.column_info_list = d['column_info_list']
        if 'field_rule_list' in d:
            o.field_rule_list = d['field_rule_list']
        if 'mdcode_notify_conf' in d:
            o.mdcode_notify_conf = d['mdcode_notify_conf']
        if 'open_card_conf' in d:
            o.open_card_conf = d['open_card_conf']
        if 'pub_channels' in d:
            o.pub_channels = d['pub_channels']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        if 'template_benefit_info' in d:
            o.template_benefit_info = d['template_benefit_info']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_style_info' in d:
            o.template_style_info = d['template_style_info']
        if 'write_off_type' in d:
            o.write_off_type = d['write_off_type']
        return o


