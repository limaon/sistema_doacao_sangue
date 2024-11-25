% ----------------------------
% Base de Conhecimento para Doacao de Sangue
% ----------------------------

% Fatos
% tiposanguineo(Nome, Tipo).
tiposanguineo(joao, a).
tiposanguineo(davi, a).
tiposanguineo(maria, a).
tiposanguineo(ana, a).
tiposanguineo(julia, o).
tiposanguineo(alice, a).
tiposanguineo(pedro, a).
tiposanguineo(laura, b).
tiposanguineo(manuela, b).
tiposanguineo(vitoria, b).
tiposanguineo(manuel, o).
tiposanguineo(jose, ab).
tiposanguineo(carlos, ab).
tiposanguineo(telma, o).

% fatorrh(Nome, Rh).
fatorrh(joao, '+').
fatorrh(davi, '+').
fatorrh(maria, '-').
fatorrh(ana, '-').
fatorrh(julia, '+').
fatorrh(alice, '+').
fatorrh(pedro, '-').
fatorrh(laura, '+').
fatorrh(manuela, '-').
fatorrh(vitoria, '+').
fatorrh(manuel, '+').
fatorrh(jose, '+').
fatorrh(carlos, '-').
fatorrh(telma, '-').

% peso(Nome, Peso).
peso(joao, 75.7).
peso(davi, 50).
peso(maria, 49).
peso(ana, 80).
peso(julia, 47).
peso(alice, 30).
peso(pedro, 20).
peso(laura, 54).
peso(manuela, 61).
peso(vitoria, 70).
peso(manuel, 130).
peso(jose, 65).
peso(carlos, 48).
peso(telma, 79).

% idade(Nome, Idade).
idade(joao, 41).
idade(davi, 24).
idade(maria, 51).
idade(ana, 17).
idade(julia, 15).
idade(alice, 56).
idade(pedro, 10).
idade(laura, 18).
idade(manuela, 66).
idade(vitoria, 12).
idade(manuel, 56).
idade(jose, 100).
idade(carlos, 67).
idade(telma, 48).

% Regras

% compativel(Doador, Receptor) - Determina se o tipo sanguíneo é compatível.
compativel(Doador, Receptor) :-
    tiposanguineo(Doador, TipoD),
    tiposanguineo(Receptor, TipoR),
    compatibilidade_tipo(TipoD, TipoR).

% compatibilidade_tipo(TipoD, TipoR) - Regras de compatibilidade ABO.
compatibilidade_tipo(a, a).
compatibilidade_tipo(a, ab).
compatibilidade_tipo(b, b).
compatibilidade_tipo(b, ab).
compatibilidade_tipo(o, a).
compatibilidade_tipo(o, b).
compatibilidade_tipo(o, ab).
compatibilidade_tipo(o, o).
compatibilidade_tipo(ab, ab).

% rh_compativel(Doador, Receptor) - Determina se o fator Rh é compatível.
rh_compativel(Doador, Receptor) :-
    fatorrh(Doador, RhD),
    fatorrh(Receptor, RhR),
    ( RhD = '-' ; (RhD = '+', RhR = '+') ).

% podedoar(Doador, Receptor) - Regra principal para determinar se um doador pode doar para um receptor.
podedoar(Doador, Receptor) :-
    compativel(Doador, Receptor),
    rh_compativel(Doador, Receptor),
    idade(Doador, Idade),
    peso(Doador, Peso),
    Idade >= 18,
    Idade =< 65,
    Peso > 50.

% pode_receber(Receptor, Doador) - Verifica se um receptor pode receber de um doador.
pode_receber(Receptor, Doador) :-
    podedoar(Doador, Receptor).

% pode_doar_para(Doador, Receptor) - Verifica se um doador pode doar para um receptor.
pode_doar_para(Doador, Receptor) :-
    podedoar(Doador, Receptor).

% esta_apto_para_qualquer_receptor(Doador) - Verifica se o doador pode doar para pelo menos um receptor.
esta_apto_para_qualquer_receptor(Doador) :-
    podedoar(Doador, _).

% doadores_com_tipo(Tipo) - Lista doadores com um determinado tipo sanguíneo.
doadores_com_tipo(Tipo, Nome) :-
    tiposanguineo(Nome, Tipo).

% doadores_com_rh(Rh, Nome) - Lista doadores com um determinado fator Rh.
doadores_com_rh(Rh, Nome) :-
    fatorrh(Nome, Rh).

% para_quem_pode_doar(Doador, Receptor) - Lista todos os receptores para quem o doador pode doar.
para_quem_pode_doar(Doador, Receptor) :-
    pode_doar_para(Doador, Receptor).

% de_quem_pode_receber(Receptor, Doador) - Lista todos os doadores de quem o receptor pode receber.
de_quem_pode_receber(Receptor, Doador) :-
    pode_receber(Receptor, Doador).
