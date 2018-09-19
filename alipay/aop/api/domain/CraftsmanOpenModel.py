#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CraftsmanAssessment import CraftsmanAssessment
from alipay.aop.api.domain.CraftsmanShopRelationOpenModel import CraftsmanShopRelationOpenModel


class CraftsmanOpenModel(object):

    def __init__(self):
        self._account = None
        self._assessment = None
        self._avatar = None
        self._career_begin = None
        self._careers = None
        self._craftsman_id = None
        self._introduction = None
        self._name = None
        self._nick_name = None
        self._operator_id = None
        self._out_craftsman_id = None
        self._qr_code = None
        self._shop_relations = None
        self._specialities = None
        self._status = None
        self._tel_num = None
        self._title = None
        self._user_id = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def assessment(self):
        return self._assessment

    @assessment.setter
    def assessment(self, value):
        if isinstance(value, CraftsmanAssessment):
            self._assessment = value
        else:
            self._assessment = CraftsmanAssessment.from_alipay_dict(value)
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
    def craftsman_id(self):
        return self._craftsman_id

    @craftsman_id.setter
    def craftsman_id(self, value):
        self._craftsman_id = value
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
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_craftsman_id(self):
        return self._out_craftsman_id

    @out_craftsman_id.setter
    def out_craftsman_id(self, value):
        self._out_craftsman_id = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
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
        if isinstance(value, list):
            self._specialities = list()
            for i in value:
                self._specialities.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.assessment:
            if hasattr(self.assessment, 'to_alipay_dict'):
                params['assessment'] = self.assessment.to_alipay_dict()
            else:
                params['assessment'] = self.assessment
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
        if self.craftsman_id:
            if hasattr(self.craftsman_id, 'to_alipay_dict'):
                params['craftsman_id'] = self.craftsman_id.to_alipay_dict()
            else:
                params['craftsman_id'] = self.craftsman_id
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
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_craftsman_id:
            if hasattr(self.out_craftsman_id, 'to_alipay_dict'):
                params['out_craftsman_id'] = self.out_craftsman_id.to_alipay_dict()
            else:
                params['out_craftsman_id'] = self.out_craftsman_id
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
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
            if isinstance(self.specialities, list):
                for i in range(0, len(self.specialities)):
                    element = self.specialities[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.specialities[i] = element.to_alipay_dict()
            if hasattr(self.specialities, 'to_alipay_dict'):
                params['specialities'] = self.specialities.to_alipay_dict()
            else:
                params['specialities'] = self.specialities
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CraftsmanOpenModel()
        if 'account' in d:
            o.account = d['account']
        if 'assessment' in d:
            o.assessment = d['assessment']
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'career_begin' in d:
            o.career_begin = d['career_begin']
        if 'careers' in d:
            o.careers = d['careers']
        if 'craftsman_id' in d:
            o.craftsman_id = d['craftsman_id']
        if 'introduction' in d:
            o.introduction = d['introduction']
        if 'name' in d:
            o.name = d['name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_craftsman_id' in d:
            o.out_craftsman_id = d['out_craftsman_id']
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        if 'shop_relations' in d:
            o.shop_relations = d['shop_relations']
        if 'specialities' in d:
            o.specialities = d['specialities']
        if 'status' in d:
            o.status = d['status']
        if 'tel_num' in d:
            o.tel_num = d['tel_num']
        if 'title' in d:
            o.title = d['title']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


