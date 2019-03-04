#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CraftsmanShopRelationOpenModel import CraftsmanShopRelationOpenModel


class KoubeiCraftsmanDataProviderCreateModel(object):

    def __init__(self):
        self._account = None
        self._auth_code = None
        self._avatar = None
        self._career_begin = None
        self._careers = None
        self._introduction = None
        self._name = None
        self._nick_name = None
        self._out_craftsman_id = None
        self._shop_relations = None
        self._specialities = None
        self._tel_num = None
        self._title = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def career_begin(self):
        return self._career_begin

    @career_begin.setter
    def career_begin(self, value):
        self._career_begin = value
    @property
    def careers(self):
        return self._careers

    @careers.setter
    def careers(self, value):
        if isinstance(value, list):
            self._careers = list()
            for i in value:
                self._careers.append(i)
    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def out_craftsman_id(self):
        return self._out_craftsman_id

    @out_craftsman_id.setter
    def out_craftsman_id(self, value):
        self._out_craftsman_id = value
    @property
    def shop_relations(self):
        return self._shop_relations

    @shop_relations.setter
    def shop_relations(self, value):
        if isinstance(value, list):
            self._shop_relations = list()
            for i in value:
                if isinstance(i, CraftsmanShopRelationOpenModel):
                    self._shop_relations.append(i)
                else:
                    self._shop_relations.append(CraftsmanShopRelationOpenModel.from_alipay_dict(i))
    @property
    def specialities(self):
        return self._specialities

    @specialities.setter
    def specialities(self, value):
        self._specialities = value
    @property
    def tel_num(self):
        return self._tel_num

    @tel_num.setter
    def tel_num(self, value):
        self._tel_num = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
        if self.career_begin:
            if hasattr(self.career_begin, 'to_alipay_dict'):
                params['career_begin'] = self.career_begin.to_alipay_dict()
            else:
                params['career_begin'] = self.career_begin
        if self.careers:
            if isinstance(self.careers, list):
                for i in range(0, len(self.careers)):
                    element = self.careers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.careers[i] = element.to_alipay_dict()
            if hasattr(self.careers, 'to_alipay_dict'):
                params['careers'] = self.careers.to_alipay_dict()
            else:
                params['careers'] = self.careers
        if self.introduction:
            if hasattr(self.introduction, 'to_alipay_dict'):
                params['introduction'] = self.introduction.to_alipay_dict()
            else:
                params['introduction'] = self.introduction
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.out_craftsman_id:
            if hasattr(self.out_craftsman_id, 'to_alipay_dict'):
                params['out_craftsman_id'] = self.out_craftsman_id.to_alipay_dict()
            else:
                params['out_craftsman_id'] = self.out_craftsman_id
        if self.shop_relations:
            if isinstance(self.shop_relations, list):
                for i in range(0, len(self.shop_relations)):
                    element = self.shop_relations[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_relations[i] = element.to_alipay_dict()
            if hasattr(self.shop_relations, 'to_alipay_dict'):
                params['shop_relations'] = self.shop_relations.to_alipay_dict()
            else:
                params['shop_relations'] = self.shop_relations
        if self.specialities:
            if hasattr(self.specialities, 'to_alipay_dict'):
                params['specialities'] = self.specialities.to_alipay_dict()
            else:
                params['specialities'] = self.specialities
        if self.tel_num:
            if hasattr(self.tel_num, 'to_alipay_dict'):
                params['tel_num'] = self.tel_num.to_alipay_dict()
            else:
                params['tel_num'] = self.tel_num
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCraftsmanDataProviderCreateModel()
        if 'account' in d:
            o.account = d['account']
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'career_begin' in d:
            o.career_begin = d['career_begin']
        if 'careers' in d:
            o.careers = d['careers']
        if 'introduction' in d:
            o.introduction = d['introduction']
        if 'name' in d:
            o.name = d['name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'out_craftsman_id' in d:
            o.out_craftsman_id = d['out_craftsman_id']
        if 'shop_relations' in d:
            o.shop_relations = d['shop_relations']
        if 'specialities' in d:
            o.specialities = d['specialities']
        if 'tel_num' in d:
            o.tel_num = d['tel_num']
        if 'title' in d:
            o.title = d['title']
        return o


