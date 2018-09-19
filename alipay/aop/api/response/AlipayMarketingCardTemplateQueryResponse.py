#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateActionInfoDTO import TemplateActionInfoDTO
from alipay.aop.api.domain.TemplateCardLevelConfDTO import TemplateCardLevelConfDTO
from alipay.aop.api.domain.TemplateColumnInfoDTO import TemplateColumnInfoDTO
from alipay.aop.api.domain.TemplateFieldRuleDTO import TemplateFieldRuleDTO
from alipay.aop.api.domain.TemplateMdcodeNotifyConfDTO import TemplateMdcodeNotifyConfDTO
from alipay.aop.api.domain.TemplateOpenCardConfDTO import TemplateOpenCardConfDTO
from alipay.aop.api.domain.PubChannelDTO import PubChannelDTO
from alipay.aop.api.domain.TemplateBenefitInfoDTO import TemplateBenefitInfoDTO
from alipay.aop.api.domain.TemplateStyleInfoDTO import TemplateStyleInfoDTO


class AlipayMarketingCardTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCardTemplateQueryResponse, self).__init__()
        self._biz_no_prefix = None
        self._biz_no_suffix_len = None
        self._card_action_list = None
        self._card_level_confs = None
        self._card_spec_tag = None
        self._card_type = None
        self._column_info_list = None
        self._field_rule_list = None
        self._mdcode_notify_conf = None
        self._open_card_conf = None
        self._pub_channels = None
        self._service_label_list = None
        self._shop_ids = None
        self._template_benefit_info = None
        self._template_style_info = None

    @property
    def biz_no_prefix(self):
        return self._biz_no_prefix

    @biz_no_prefix.setter
    def biz_no_prefix(self, value):
        self._biz_no_prefix = value
    @property
    def biz_no_suffix_len(self):
        return self._biz_no_suffix_len

    @biz_no_suffix_len.setter
    def biz_no_suffix_len(self, value):
        self._biz_no_suffix_len = value
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
    def card_level_confs(self):
        return self._card_level_confs

    @card_level_confs.setter
    def card_level_confs(self, value):
        if isinstance(value, list):
            self._card_level_confs = list()
            for i in value:
                if isinstance(i, TemplateCardLevelConfDTO):
                    self._card_level_confs.append(i)
                else:
                    self._card_level_confs.append(TemplateCardLevelConfDTO.from_alipay_dict(i))
    @property
    def card_spec_tag(self):
        return self._card_spec_tag

    @card_spec_tag.setter
    def card_spec_tag(self, value):
        self._card_spec_tag = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
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
    def service_label_list(self):
        return self._service_label_list

    @service_label_list.setter
    def service_label_list(self, value):
        if isinstance(value, list):
            self._service_label_list = list()
            for i in value:
                self._service_label_list.append(i)
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
    def template_style_info(self):
        return self._template_style_info

    @template_style_info.setter
    def template_style_info(self, value):
        if isinstance(value, TemplateStyleInfoDTO):
            self._template_style_info = value
        else:
            self._template_style_info = TemplateStyleInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCardTemplateQueryResponse, self).parse_response_content(response_content)
        if 'biz_no_prefix' in response:
            self.biz_no_prefix = response['biz_no_prefix']
        if 'biz_no_suffix_len' in response:
            self.biz_no_suffix_len = response['biz_no_suffix_len']
        if 'card_action_list' in response:
            self.card_action_list = response['card_action_list']
        if 'card_level_confs' in response:
            self.card_level_confs = response['card_level_confs']
        if 'card_spec_tag' in response:
            self.card_spec_tag = response['card_spec_tag']
        if 'card_type' in response:
            self.card_type = response['card_type']
        if 'column_info_list' in response:
            self.column_info_list = response['column_info_list']
        if 'field_rule_list' in response:
            self.field_rule_list = response['field_rule_list']
        if 'mdcode_notify_conf' in response:
            self.mdcode_notify_conf = response['mdcode_notify_conf']
        if 'open_card_conf' in response:
            self.open_card_conf = response['open_card_conf']
        if 'pub_channels' in response:
            self.pub_channels = response['pub_channels']
        if 'service_label_list' in response:
            self.service_label_list = response['service_label_list']
        if 'shop_ids' in response:
            self.shop_ids = response['shop_ids']
        if 'template_benefit_info' in response:
            self.template_benefit_info = response['template_benefit_info']
        if 'template_style_info' in response:
            self.template_style_info = response['template_style_info']
