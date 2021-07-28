#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MemberRule import MemberRule


class ZhimaCreditPeZmgoTemplateCreateModel(object):

    def __init__(self):
        self._benefit_url = None
        self._biz_no = None
        self._consume_pid_list = None
        self._contact = None
        self._ext_info = None
        self._member_agreement = None
        self._member_mode = None
        self._member_rule = None
        self._partner_id = None
        self._template_name = None

    @property
    def benefit_url(self):
        return self._benefit_url

    @benefit_url.setter
    def benefit_url(self, value):
        self._benefit_url = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def consume_pid_list(self):
        return self._consume_pid_list

    @consume_pid_list.setter
    def consume_pid_list(self, value):
        if isinstance(value, list):
            self._consume_pid_list = list()
            for i in value:
                self._consume_pid_list.append(i)
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def member_agreement(self):
        return self._member_agreement

    @member_agreement.setter
    def member_agreement(self, value):
        self._member_agreement = value
    @property
    def member_mode(self):
        return self._member_mode

    @member_mode.setter
    def member_mode(self, value):
        self._member_mode = value
    @property
    def member_rule(self):
        return self._member_rule

    @member_rule.setter
    def member_rule(self, value):
        if isinstance(value, MemberRule):
            self._member_rule = value
        else:
            self._member_rule = MemberRule.from_alipay_dict(value)
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_url:
            if hasattr(self.benefit_url, 'to_alipay_dict'):
                params['benefit_url'] = self.benefit_url.to_alipay_dict()
            else:
                params['benefit_url'] = self.benefit_url
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.consume_pid_list:
            if isinstance(self.consume_pid_list, list):
                for i in range(0, len(self.consume_pid_list)):
                    element = self.consume_pid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.consume_pid_list[i] = element.to_alipay_dict()
            if hasattr(self.consume_pid_list, 'to_alipay_dict'):
                params['consume_pid_list'] = self.consume_pid_list.to_alipay_dict()
            else:
                params['consume_pid_list'] = self.consume_pid_list
        if self.contact:
            if hasattr(self.contact, 'to_alipay_dict'):
                params['contact'] = self.contact.to_alipay_dict()
            else:
                params['contact'] = self.contact
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.member_agreement:
            if hasattr(self.member_agreement, 'to_alipay_dict'):
                params['member_agreement'] = self.member_agreement.to_alipay_dict()
            else:
                params['member_agreement'] = self.member_agreement
        if self.member_mode:
            if hasattr(self.member_mode, 'to_alipay_dict'):
                params['member_mode'] = self.member_mode.to_alipay_dict()
            else:
                params['member_mode'] = self.member_mode
        if self.member_rule:
            if hasattr(self.member_rule, 'to_alipay_dict'):
                params['member_rule'] = self.member_rule.to_alipay_dict()
            else:
                params['member_rule'] = self.member_rule
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeZmgoTemplateCreateModel()
        if 'benefit_url' in d:
            o.benefit_url = d['benefit_url']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'consume_pid_list' in d:
            o.consume_pid_list = d['consume_pid_list']
        if 'contact' in d:
            o.contact = d['contact']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'member_agreement' in d:
            o.member_agreement = d['member_agreement']
        if 'member_mode' in d:
            o.member_mode = d['member_mode']
        if 'member_rule' in d:
            o.member_rule = d['member_rule']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        return o


