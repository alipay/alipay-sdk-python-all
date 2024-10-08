#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Discount import Discount
from alipay.aop.api.domain.LuggagePolicy import LuggagePolicy
from alipay.aop.api.domain.Policy import Policy
from alipay.aop.api.domain.Policy import Policy
from alipay.aop.api.domain.ReimbursementPolicy import ReimbursementPolicy
from alipay.aop.api.domain.SaleControl import SaleControl


class Cabin(object):

    def __init__(self):
        self._adult_discount_price = None
        self._adult_price = None
        self._cabin_code = None
        self._cabin_discount = None
        self._cabin_name = None
        self._child_price = None
        self._discount_list = None
        self._discount_tag = None
        self._fuel_cost = None
        self._infant_price = None
        self._infrastructure_cost = None
        self._link_url = None
        self._luggage_policies = None
        self._meal = None
        self._rebook_policies = None
        self._refund_policies = None
        self._reimbursement_policies = None
        self._sale_controls = None
        self._ticket_count = None

    @property
    def adult_discount_price(self):
        return self._adult_discount_price

    @adult_discount_price.setter
    def adult_discount_price(self, value):
        self._adult_discount_price = value
    @property
    def adult_price(self):
        return self._adult_price

    @adult_price.setter
    def adult_price(self, value):
        self._adult_price = value
    @property
    def cabin_code(self):
        return self._cabin_code

    @cabin_code.setter
    def cabin_code(self, value):
        self._cabin_code = value
    @property
    def cabin_discount(self):
        return self._cabin_discount

    @cabin_discount.setter
    def cabin_discount(self, value):
        self._cabin_discount = value
    @property
    def cabin_name(self):
        return self._cabin_name

    @cabin_name.setter
    def cabin_name(self, value):
        self._cabin_name = value
    @property
    def child_price(self):
        return self._child_price

    @child_price.setter
    def child_price(self, value):
        self._child_price = value
    @property
    def discount_list(self):
        return self._discount_list

    @discount_list.setter
    def discount_list(self, value):
        if isinstance(value, list):
            self._discount_list = list()
            for i in value:
                if isinstance(i, Discount):
                    self._discount_list.append(i)
                else:
                    self._discount_list.append(Discount.from_alipay_dict(i))
    @property
    def discount_tag(self):
        return self._discount_tag

    @discount_tag.setter
    def discount_tag(self, value):
        self._discount_tag = value
    @property
    def fuel_cost(self):
        return self._fuel_cost

    @fuel_cost.setter
    def fuel_cost(self, value):
        self._fuel_cost = value
    @property
    def infant_price(self):
        return self._infant_price

    @infant_price.setter
    def infant_price(self, value):
        self._infant_price = value
    @property
    def infrastructure_cost(self):
        return self._infrastructure_cost

    @infrastructure_cost.setter
    def infrastructure_cost(self, value):
        self._infrastructure_cost = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def luggage_policies(self):
        return self._luggage_policies

    @luggage_policies.setter
    def luggage_policies(self, value):
        if isinstance(value, list):
            self._luggage_policies = list()
            for i in value:
                if isinstance(i, LuggagePolicy):
                    self._luggage_policies.append(i)
                else:
                    self._luggage_policies.append(LuggagePolicy.from_alipay_dict(i))
    @property
    def meal(self):
        return self._meal

    @meal.setter
    def meal(self, value):
        self._meal = value
    @property
    def rebook_policies(self):
        return self._rebook_policies

    @rebook_policies.setter
    def rebook_policies(self, value):
        if isinstance(value, list):
            self._rebook_policies = list()
            for i in value:
                if isinstance(i, Policy):
                    self._rebook_policies.append(i)
                else:
                    self._rebook_policies.append(Policy.from_alipay_dict(i))
    @property
    def refund_policies(self):
        return self._refund_policies

    @refund_policies.setter
    def refund_policies(self, value):
        if isinstance(value, list):
            self._refund_policies = list()
            for i in value:
                if isinstance(i, Policy):
                    self._refund_policies.append(i)
                else:
                    self._refund_policies.append(Policy.from_alipay_dict(i))
    @property
    def reimbursement_policies(self):
        return self._reimbursement_policies

    @reimbursement_policies.setter
    def reimbursement_policies(self, value):
        if isinstance(value, list):
            self._reimbursement_policies = list()
            for i in value:
                if isinstance(i, ReimbursementPolicy):
                    self._reimbursement_policies.append(i)
                else:
                    self._reimbursement_policies.append(ReimbursementPolicy.from_alipay_dict(i))
    @property
    def sale_controls(self):
        return self._sale_controls

    @sale_controls.setter
    def sale_controls(self, value):
        if isinstance(value, list):
            self._sale_controls = list()
            for i in value:
                if isinstance(i, SaleControl):
                    self._sale_controls.append(i)
                else:
                    self._sale_controls.append(SaleControl.from_alipay_dict(i))
    @property
    def ticket_count(self):
        return self._ticket_count

    @ticket_count.setter
    def ticket_count(self, value):
        self._ticket_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.adult_discount_price:
            if hasattr(self.adult_discount_price, 'to_alipay_dict'):
                params['adult_discount_price'] = self.adult_discount_price.to_alipay_dict()
            else:
                params['adult_discount_price'] = self.adult_discount_price
        if self.adult_price:
            if hasattr(self.adult_price, 'to_alipay_dict'):
                params['adult_price'] = self.adult_price.to_alipay_dict()
            else:
                params['adult_price'] = self.adult_price
        if self.cabin_code:
            if hasattr(self.cabin_code, 'to_alipay_dict'):
                params['cabin_code'] = self.cabin_code.to_alipay_dict()
            else:
                params['cabin_code'] = self.cabin_code
        if self.cabin_discount:
            if hasattr(self.cabin_discount, 'to_alipay_dict'):
                params['cabin_discount'] = self.cabin_discount.to_alipay_dict()
            else:
                params['cabin_discount'] = self.cabin_discount
        if self.cabin_name:
            if hasattr(self.cabin_name, 'to_alipay_dict'):
                params['cabin_name'] = self.cabin_name.to_alipay_dict()
            else:
                params['cabin_name'] = self.cabin_name
        if self.child_price:
            if hasattr(self.child_price, 'to_alipay_dict'):
                params['child_price'] = self.child_price.to_alipay_dict()
            else:
                params['child_price'] = self.child_price
        if self.discount_list:
            if isinstance(self.discount_list, list):
                for i in range(0, len(self.discount_list)):
                    element = self.discount_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_list[i] = element.to_alipay_dict()
            if hasattr(self.discount_list, 'to_alipay_dict'):
                params['discount_list'] = self.discount_list.to_alipay_dict()
            else:
                params['discount_list'] = self.discount_list
        if self.discount_tag:
            if hasattr(self.discount_tag, 'to_alipay_dict'):
                params['discount_tag'] = self.discount_tag.to_alipay_dict()
            else:
                params['discount_tag'] = self.discount_tag
        if self.fuel_cost:
            if hasattr(self.fuel_cost, 'to_alipay_dict'):
                params['fuel_cost'] = self.fuel_cost.to_alipay_dict()
            else:
                params['fuel_cost'] = self.fuel_cost
        if self.infant_price:
            if hasattr(self.infant_price, 'to_alipay_dict'):
                params['infant_price'] = self.infant_price.to_alipay_dict()
            else:
                params['infant_price'] = self.infant_price
        if self.infrastructure_cost:
            if hasattr(self.infrastructure_cost, 'to_alipay_dict'):
                params['infrastructure_cost'] = self.infrastructure_cost.to_alipay_dict()
            else:
                params['infrastructure_cost'] = self.infrastructure_cost
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.luggage_policies:
            if isinstance(self.luggage_policies, list):
                for i in range(0, len(self.luggage_policies)):
                    element = self.luggage_policies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.luggage_policies[i] = element.to_alipay_dict()
            if hasattr(self.luggage_policies, 'to_alipay_dict'):
                params['luggage_policies'] = self.luggage_policies.to_alipay_dict()
            else:
                params['luggage_policies'] = self.luggage_policies
        if self.meal:
            if hasattr(self.meal, 'to_alipay_dict'):
                params['meal'] = self.meal.to_alipay_dict()
            else:
                params['meal'] = self.meal
        if self.rebook_policies:
            if isinstance(self.rebook_policies, list):
                for i in range(0, len(self.rebook_policies)):
                    element = self.rebook_policies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rebook_policies[i] = element.to_alipay_dict()
            if hasattr(self.rebook_policies, 'to_alipay_dict'):
                params['rebook_policies'] = self.rebook_policies.to_alipay_dict()
            else:
                params['rebook_policies'] = self.rebook_policies
        if self.refund_policies:
            if isinstance(self.refund_policies, list):
                for i in range(0, len(self.refund_policies)):
                    element = self.refund_policies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_policies[i] = element.to_alipay_dict()
            if hasattr(self.refund_policies, 'to_alipay_dict'):
                params['refund_policies'] = self.refund_policies.to_alipay_dict()
            else:
                params['refund_policies'] = self.refund_policies
        if self.reimbursement_policies:
            if isinstance(self.reimbursement_policies, list):
                for i in range(0, len(self.reimbursement_policies)):
                    element = self.reimbursement_policies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.reimbursement_policies[i] = element.to_alipay_dict()
            if hasattr(self.reimbursement_policies, 'to_alipay_dict'):
                params['reimbursement_policies'] = self.reimbursement_policies.to_alipay_dict()
            else:
                params['reimbursement_policies'] = self.reimbursement_policies
        if self.sale_controls:
            if isinstance(self.sale_controls, list):
                for i in range(0, len(self.sale_controls)):
                    element = self.sale_controls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sale_controls[i] = element.to_alipay_dict()
            if hasattr(self.sale_controls, 'to_alipay_dict'):
                params['sale_controls'] = self.sale_controls.to_alipay_dict()
            else:
                params['sale_controls'] = self.sale_controls
        if self.ticket_count:
            if hasattr(self.ticket_count, 'to_alipay_dict'):
                params['ticket_count'] = self.ticket_count.to_alipay_dict()
            else:
                params['ticket_count'] = self.ticket_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Cabin()
        if 'adult_discount_price' in d:
            o.adult_discount_price = d['adult_discount_price']
        if 'adult_price' in d:
            o.adult_price = d['adult_price']
        if 'cabin_code' in d:
            o.cabin_code = d['cabin_code']
        if 'cabin_discount' in d:
            o.cabin_discount = d['cabin_discount']
        if 'cabin_name' in d:
            o.cabin_name = d['cabin_name']
        if 'child_price' in d:
            o.child_price = d['child_price']
        if 'discount_list' in d:
            o.discount_list = d['discount_list']
        if 'discount_tag' in d:
            o.discount_tag = d['discount_tag']
        if 'fuel_cost' in d:
            o.fuel_cost = d['fuel_cost']
        if 'infant_price' in d:
            o.infant_price = d['infant_price']
        if 'infrastructure_cost' in d:
            o.infrastructure_cost = d['infrastructure_cost']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'luggage_policies' in d:
            o.luggage_policies = d['luggage_policies']
        if 'meal' in d:
            o.meal = d['meal']
        if 'rebook_policies' in d:
            o.rebook_policies = d['rebook_policies']
        if 'refund_policies' in d:
            o.refund_policies = d['refund_policies']
        if 'reimbursement_policies' in d:
            o.reimbursement_policies = d['reimbursement_policies']
        if 'sale_controls' in d:
            o.sale_controls = d['sale_controls']
        if 'ticket_count' in d:
            o.ticket_count = d['ticket_count']
        return o


