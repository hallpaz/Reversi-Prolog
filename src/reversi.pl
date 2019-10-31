replace([_|T], 0, X, [X|T]).
replace([H|T], I, X, [H|R]):- I > 0, I1 is I-1, replace(T, I1, X, R).

element_at(0,[X|_],X).
element_at(K,[_|L],X) :- 
	K>0,
	K1 is K-1, 
	element_at(K1,L,X).


element_at( X, Y, M, El) :-
	element_at( X, M, Lin),
	element_at( Y, Lin, El).

novotab([	[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,1,2,0,0,0],
		[0,0,0,2,1,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]
	]):-!.

writeTab([X|Tab]):-
	write(X),nl,
	writeTab(Tab).

writeTab([]).

invert_color(Cor,CorInv):-
	Cor=:=1->CorInv is 2;
	Cor=:=2->CorInv is 1.


change_color_at(Mold,I,J,NCor,Mat):-
	replace(Mold,I,NL,Mat),
	replace(OL,J,NCor,NL),
	element_at(I,Mold,OL).

check_play_W(Tab,I,J,Cor,F,X):-
	not(J=:=0),
	J1 is J-1,
	element_at(I,J1,Tab,CorW),
	(CorW=:=Cor->
		(F=:=0->false;
			X is J1,true
		);
	CorW=:=0->false;
	check_play_W(Tab,I,J1,Cor,1,X)
	).

check_play_E(Tab,I,J,Cor,F,X):-
	not(J=:=7),	
	J1 is J+1,
	element_at(I,J1,Tab,CorW),
	(CorW=:=Cor->
		(F=:=0->false;
			X is J1,true
		);
	CorW=:=0->false;
	check_play_E(Tab,I,J1,Cor,1,X)
	).

check_play_N(Tab,I,J,Cor,F,Y):-
	not(I=:=0),	
	I1 is I-1,
	element_at(I1,J,Tab,CorW),
	(CorW=:=Cor->
		(F=:=0->false;
			Y is I1,true
		);
	CorW=:=0->false;
	check_play_N(Tab,I1,J,Cor,1,Y)
	).

check_play_S(Tab,I,J,Cor,F,Y):-
	not(I=:=7),	
	I1 is I+1,
	element_at(I1,J,Tab,CorW),
	(CorW=:=Cor->
		(F=:=0->false;
			Y is I1,true
		);
	CorW=:=0->false;
	check_play_S(Tab,I1,J,Cor,1,Y)
	).

check_play_NW(Tab,I,J,Cor,F,X,Y):-
	not(I=:=0),not(J=:=0),	
	I1 is I-1,J1 is J-1,
	element_at(I1,J1,Tab,CorW),
	(CorW=:=Cor->
		(F=:=0->
			false;
			Y is I1,X is J1,true
		);
		(CorW=:=0->
			false;
			check_play_NW(Tab,I1,J1,Cor,1,X,Y)
		)
	).

check_play_NE(Tab,I,J,Cor,F,X):-
	not(I=:=0),not(J=:=7),	
	I1 is I-1,J1 is J+1,
	element_at(I1,J1,Tab,CorW),
	(CorW=:=Cor->
		(F=:=0->
			false;
			X is J1,true
		);
		(CorW=:=0->	
			false;
			check_play_NE(Tab,I1,J1,Cor,1,X)
		)
	).


check_play_SW(Tab,I,J,Cor,F,X,Y):-
	not(I=:=7),not(J=:=0),
	I1 is I+1,J1 is J-1,
	element_at(I1,J1,Tab,CorW),
	(CorW=:=Cor->
		(F=:=0->
			false;
			X is J1,Y is I1,true
		);
		(CorW=:=0->
			false;
			check_play_SW(Tab,I1,J1,Cor,1,X,Y)
		)
	).

check_play_SE(Tab,I,J,Cor,F,X):-
	not(I=:=7),not(J=:=7),
	I1 is I+1,J1 is J+1,
	element_at(I1,J1,Tab,CorW),
	(CorW=:=Cor->
		(F=:=0->
			false;
			X is J1,true
		);
		(CorW=:=0->
			false;
			check_play_SE(Tab,I1,J1,Cor,1,X)
		)
	).

check_play(Tab,I,J,Cor,P):-(
		not(element_at(I,J,Tab,1)),
		not(element_at(I,J,Tab,2))
	),(
		(check_play_W(Tab,I,J,Cor,0,X) -> PW is J-X; PW is 0),
		(check_play_E(Tab,I,J,Cor,0,X) -> PE is X-J; PE is 0),
		(check_play_N(Tab,I,J,Cor,0,Y) -> PN is I-Y; PN is 0),
		(check_play_S(Tab,I,J,Cor,0,Y) -> PS is Y-I; PS is 0),
		(check_play_NW(Tab,I,J,Cor,0,X,Y) -> PNW is J-X; PNW is 0),
		(check_play_NE(Tab,I,J,Cor,0,X) -> PNE is X-J; PNE is 0),
		(check_play_SW(Tab,I,J,Cor,0,X,Y) -> PSW is J-X; PSW is 0),
		(check_play_SE(Tab,I,J,Cor,0,X) -> PSE is X-J; PSE is 0),
		P is PW+PE+PN+PS+PNW+PNE+PSW+PSE, (P=:=0 -> false; true)
	).	

%invert_color_In_to_Fi(I,In,Fi,Tab,TabN):-
	

change_color_line_In_to_Fi(I,In,Fi,NCor,Tab,TabN):-
	change_color_at(Tab,I,In,NCor,TabI),
	(
	not(In=:=Fi) -> 
		In1 is In+1,change_color_line_In_to_Fi(I,In1,Fi,NCor,TabI,TabN);
		copy_tab(TabI,TabN)
	).

change_color_column_In_to_Fi(In,Fi,J,NCor,Tab,TabN):-
	change_color_at(Tab,In,J,NCor,TabI),
	(
	not(In=:=Fi) -> 	
		In1 is In+1,change_color_column_In_to_Fi(In1,Fi,J,NCor,TabI,TabN);
		copy_tab(TabI,TabN)
	).

change_color_diagp_In_to_Fi(I,In,Fi,NCor,Tab,TabN):-
	change_color_at(Tab,I,In,NCor,TabI),
	(
	not(In=:=Fi) -> 	
		I1 is I+1,In1 is In+1,change_color_diagp_In_to_Fi(I1,In1,Fi,NCor,TabI,TabN);
				copy_tab(TabI,TabN)
	).

change_color_diags_In_to_Fi(I,In,Fi,NCor,Tab,TabN):-
	change_color_at(Tab,I,In,NCor,TabI),
	(
	not(In=:=Fi) -> 	
		I1 is I-1,In1 is In+1,change_color_diags_In_to_Fi(I1,In1,Fi,NCor,TabI,TabN);
		copy_tab(TabI,TabN)
	).


copy_tab(L,R) :- accCp(L,R).
accCp([],[]).
accCp([H|T1],[H|T2]) :- accCp(T1,T2).

play_W(Tab,I,J,Cor,TabN):-
	(check_play_W(Tab,I,J,Cor,0,X) ->	change_color_line_In_to_Fi(I,X,J,Cor,Tab,TabN);
						copy_tab(Tab,TabN)
					).

play_E(Tab,I,J,Cor,TabN):-
	(check_play_E(Tab,I,J,Cor,0,X) ->	change_color_line_In_to_Fi(I,J,X,Cor,Tab,TabN);
						copy_tab(Tab,TabN)
					).

play_N(Tab,I,J,Cor,TabN):-
	(check_play_N(Tab,I,J,Cor,0,Y) ->	change_color_column_In_to_Fi(Y,I,J,Cor,Tab,TabN);
						copy_tab(Tab,TabN)
					).

play_S(Tab,I,J,Cor,TabN):-
	(check_play_S(Tab,I,J,Cor,0,Y) ->	change_color_column_In_to_Fi(I,Y,J,Cor,Tab,TabN);
						copy_tab(Tab,TabN)
					).

play_NW(Tab,I,J,Cor,TabN):-
	(check_play_NW(Tab,I,J,Cor,0,X,Y) ->	change_color_diagp_In_to_Fi(Y,X,J,Cor,Tab,TabN);
						copy_tab(Tab,TabN)
					).

play_SE(Tab,I,J,Cor,TabN):-
	(check_play_SE(Tab,I,J,Cor,0,X) ->	change_color_diagp_In_to_Fi(I,J,X,Cor,Tab,TabN);
						copy_tab(Tab,TabN)
					).
	
play_NE(Tab,I,J,Cor,TabN):-
	(check_play_NE(Tab,I,J,Cor,0,X) ->	change_color_diags_In_to_Fi(I,J,X,Cor,Tab,TabN);
						copy_tab(Tab,TabN)
					).				

play_SW(Tab,I,J,Cor,TabN):-
	(check_play_SW(Tab,I,J,Cor,0,X,Y) ->	change_color_diags_In_to_Fi(Y,X,J,Cor,Tab,TabN);
						copy_tab(Tab,TabN)
					).


play(Tab,I,J,Cor,TabSW):-
	check_play(Tab,I,J,Cor,P),
	play_W(Tab,I,J,Cor,TabW),
      	play_E(TabW,I,J,Cor,TabE),
	play_N(TabE,I,J,Cor,TabN),
	play_S(TabN,I,J,Cor,TabS),
	play_NW(TabS,I,J,Cor,TabNW),
	play_SE(TabNW,I,J,Cor,TabSE),
	play_NE(TabSE,I,J,Cor,TabNE),
	play_SW(TabNE,I,J,Cor,TabSW).

macaco_linha(Tab,Lin,TJ,J,Cor):-
	J is TJ,check_play(Tab,Lin,TJ,Cor,P);
	not(TJ=:=7),TJ1 is TJ+1,macaco_linha(Tab,Lin,TJ1,J,Cor).

macaco(Tab,TI,I,J,Cor):-
	I is TI,macaco_linha(Tab,TI,0,J,Cor);
	not(TI=:=7),TI1 is TI+1,macaco(Tab,TI1,I,J,Cor).

macaco(Tab,I,J):-macaco(Tab,0,I,J,2).

macaco_play(Tab,TabN):-
	macaco(Tab,I,J),
	play(Tab,I,J,2,TabN).

macaco1_play(Tab,TabN):-
	macaco(Tab,0,I,J,1),
	play(Tab,I,J,1,TabN).

dont_game_over(Tab):-
	macaco(Tab,I,J);
	macaco(Tab,0,I,J,1).	

winner_line(_,_,8,P0,P1,P2):-
	P0 is 0,P1 is 0, P2 is 0.

winner_coord(Tab,I,J,P0,NP0,P1,NP1,P2,NP2):-
	element_at(I,J,Tab,Cor),
	(Cor=:=1 -> 
		NP0 is P0,NP1 is P1+1,NP2 is P2;
		(Cor=:=2 -> 
			NP0 is P0,NP1 is P1,NP2 is P2+1;
			NP0 is P0+1,NP1 is P1,NP2 is P2
		)		
	).
	
winner_line(Tab,I,P0,NP0,P1,NP1,P2,NP2):-
	winner_coord(Tab,I,0,0,P00,0,P10,0,P20),
	winner_coord(Tab,I,1,P00,P01,P10,P11,P20,P21),
	winner_coord(Tab,I,2,P01,P02,P11,P12,P21,P22),
	winner_coord(Tab,I,3,P02,P03,P12,P13,P22,P23),
	winner_coord(Tab,I,4,P03,P04,P13,P14,P23,P24),
	winner_coord(Tab,I,5,P04,P05,P14,P15,P24,P25),
	winner_coord(Tab,I,6,P05,P06,P15,P16,P25,P26),
	winner_coord(Tab,I,7,P06,P07,P16,P17,P26,P27),
	NP0 is P0+P07,NP1 is P1+P17,NP2 is P2+P27.

winner(Tab,P0,P1,P2):-
	winner_line(Tab,0,0,P00,0,P10,0,P20)
	,winner_line(Tab,1,P00,P01,P10,P11,P20,P21)
	,winner_line(Tab,2,P01,P02,P11,P12,P21,P22)
	,winner_line(Tab,3,P02,P03,P12,P13,P22,P23)
	,winner_line(Tab,4,P03,P04,P13,P14,P23,P24)
	,winner_line(Tab,5,P04,P05,P14,P15,P24,P25)
	,winner_line(Tab,6,P05,P06,P15,P16,P25,P26)
	,winner_line(Tab,7,P06,P0,P16,P1,P26,P2).

winner(Tab,V):-
	winner(Tab,_,P1,P2),
	(P1>P2 ->
		V is 1;
		(P2>P1 ->
			V is 2;
			V is 0		
		)
	).

golfinho_linha(Tab,Lin,J,P):-
	(check_play(Tab,Lin,0,2,P0) -> 
		(P0>0 -> 
			Pn1 is P0,J1 is 0;
			Pn1 is 0
		);Pn1 is 0,J1 is 0
	
	),
	(check_play(Tab,Lin,1,2,P1) -> 
		(P1>Pn1 -> 
			(Pn2 is P1,J2 is 1);
			(Pn2 is Pn1)
		);Pn2 is Pn1,J2 is J1
	),
	(check_play(Tab,Lin,2,2,P2) -> 
		(P2>Pn2 -> 
			Pn3 is P2,J3 is 2;
			Pn3 is Pn2,J3 is J2
		);
		(Pn3 is Pn2,J3 is J2)
	),
	(check_play(Tab,Lin,3,2,P3) -> 
		(P3>Pn3 -> 
			Pn4 is P3,J4 is 3;
			Pn4 is Pn3,J4 is J3
		);
		(Pn4 is Pn3,J4 is J3)
	),
	(check_play(Tab,Lin,4,2,P4) -> 
		(P4>Pn4 -> 
			Pn5 is P4,J5 is 4;
			Pn5 is Pn4,J5 is J4
		);
		(Pn5 is Pn4,J5 is J4)
	),
	(check_play(Tab,Lin,5,2,P5) -> 
		(P5>Pn5 -> 
			Pn6 is P5,J6 is 5;
			Pn6 is Pn5,J6 is J5
		);
		(Pn6 is Pn5,J6 is J5)
	),
	(check_play(Tab,Lin,6,2,P6) -> 
		(P6>Pn6 -> 
			Pn7 is P6,J7 is 6;
			Pn7 is Pn6,J7 is J6
		);
		(Pn7 is Pn6,J7 is J6)
	),
	(check_play(Tab,Lin,7,2,P7) -> 
		(P7>Pn7 -> 
			P   is P7,J is 7;
			P   is Pn7,J is J7
		);
		(P   is Pn7,J is J7)
	).

golfinho(Tab,I,J):-
	golfinho_linha(Tab,0,J0,P0),
	golfinho_linha(Tab,1,J1,P1),(P1>P0 ->  In1 is 1,Pn1 is P1,Jn1 is J1;In1 is 0,Pn1 is P0,Jn1 is J0),
	golfinho_linha(Tab,2,J2,P2),(P2>Pn1 -> In2 is 2,Pn2 is P2,Jn2 is J2;In2 is In1,Pn2 is Pn1,Jn2 is Jn1),
	golfinho_linha(Tab,3,J3,P3),(P3>Pn2 -> In3 is 3,Pn3 is P3,Jn3 is J3;In3 is In2,Pn3 is Pn2,Jn3 is Jn2),
	golfinho_linha(Tab,4,J4,P4),(P4>Pn3 -> In4 is 4,Pn4 is P4,Jn4 is J4;In4 is In3,Pn4 is Pn3,Jn4 is Jn3),
	golfinho_linha(Tab,5,J5,P5),(P5>Pn4 -> In5 is 5,Pn5 is P5,Jn5 is J5;In5 is In4,Pn5 is Pn4,Jn5 is Jn4),
	golfinho_linha(Tab,6,J6,P6),(P6>Pn5 -> In6 is 6,Pn6 is P6,Jn6 is J6;In6 is In5,Pn6 is Pn5,Jn6 is Jn5),
	golfinho_linha(Tab,7,J7,P7),(P7>Pn6 -> I   is 7,P   is P7,J   is J7;I   is In6,P   is Pn6,J   is Jn6).

golfinho_play(Tab,TabN):-
	golfinho(Tab,I,J),
	play(Tab,I,J,2,TabN).

main:-
	novotab(Tab)
	,simula_macacoXgolfinho(Tab)
.
simula_macacoXgolfinho(Tab):-
	(macaco1_play(Tab,TabM),
	golfinho_play(TabM,TabG),
	simula_macacoXgolfinho(TabG));

	(macaco1_play(Tab,TabM),
	simula_macacoXgolfinho(TabM));

	(golfinho_play(Tab,TabG),
	simula_macacoXgolfinho(TabG));
	writeTab(Tab),winner(Tab,P0,P1,P2),nl,write('Placar: Golfinho '),write(P2),nl,write('Macaco '),write(P1).
