#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QianfanCardItem import QianfanCardItem
from alipay.aop.api.domain.McpAbility import McpAbility
from alipay.aop.api.domain.SkillAbility import SkillAbility


class AbilityItem(object):

    def __init__(self):
        self._ability_code = None
        self._ability_name_en = None
        self._ability_type = None
        self._ability_version = None
        self._cards = None
        self._mcp_schema = None
        self._skill_schema = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def ability_name_en(self):
        return self._ability_name_en

    @ability_name_en.setter
    def ability_name_en(self, value):
        self._ability_name_en = value
    @property
    def ability_type(self):
        return self._ability_type

    @ability_type.setter
    def ability_type(self, value):
        self._ability_type = value
    @property
    def ability_version(self):
        return self._ability_version

    @ability_version.setter
    def ability_version(self, value):
        self._ability_version = value
    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        if isinstance(value, list):
            self._cards = list()
            for i in value:
                if isinstance(i, QianfanCardItem):
                    self._cards.append(i)
                else:
                    self._cards.append(QianfanCardItem.from_alipay_dict(i))
    @property
    def mcp_schema(self):
        return self._mcp_schema

    @mcp_schema.setter
    def mcp_schema(self, value):
        if isinstance(value, McpAbility):
            self._mcp_schema = value
        else:
            self._mcp_schema = McpAbility.from_alipay_dict(value)
    @property
    def skill_schema(self):
        return self._skill_schema

    @skill_schema.setter
    def skill_schema(self, value):
        if isinstance(value, SkillAbility):
            self._skill_schema = value
        else:
            self._skill_schema = SkillAbility.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.ability_name_en:
            if hasattr(self.ability_name_en, 'to_alipay_dict'):
                params['ability_name_en'] = self.ability_name_en.to_alipay_dict()
            else:
                params['ability_name_en'] = self.ability_name_en
        if self.ability_type:
            if hasattr(self.ability_type, 'to_alipay_dict'):
                params['ability_type'] = self.ability_type.to_alipay_dict()
            else:
                params['ability_type'] = self.ability_type
        if self.ability_version:
            if hasattr(self.ability_version, 'to_alipay_dict'):
                params['ability_version'] = self.ability_version.to_alipay_dict()
            else:
                params['ability_version'] = self.ability_version
        if self.cards:
            if isinstance(self.cards, list):
                for i in range(0, len(self.cards)):
                    element = self.cards[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cards[i] = element.to_alipay_dict()
            if hasattr(self.cards, 'to_alipay_dict'):
                params['cards'] = self.cards.to_alipay_dict()
            else:
                params['cards'] = self.cards
        if self.mcp_schema:
            if hasattr(self.mcp_schema, 'to_alipay_dict'):
                params['mcp_schema'] = self.mcp_schema.to_alipay_dict()
            else:
                params['mcp_schema'] = self.mcp_schema
        if self.skill_schema:
            if hasattr(self.skill_schema, 'to_alipay_dict'):
                params['skill_schema'] = self.skill_schema.to_alipay_dict()
            else:
                params['skill_schema'] = self.skill_schema
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AbilityItem()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'ability_name_en' in d:
            o.ability_name_en = d['ability_name_en']
        if 'ability_type' in d:
            o.ability_type = d['ability_type']
        if 'ability_version' in d:
            o.ability_version = d['ability_version']
        if 'cards' in d:
            o.cards = d['cards']
        if 'mcp_schema' in d:
            o.mcp_schema = d['mcp_schema']
        if 'skill_schema' in d:
            o.skill_schema = d['skill_schema']
        return o


